import sys
from time import sleep

from pygame.locals import *
import random, time

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

from pygame import mixer 

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        mixer.init()
        self.settings = Settings()
        #fullscreen mode
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        """a spesific screen size for the game"""
        self.flags = pygame.HWSURFACE | pygame.FULLSCREEN | pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode([self.settings.screen_width, self.settings.screen_height], self.flags, vsync=0)
        self.height = pygame.display.Info().current_h
        self.width = pygame.display.Info().current_w
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #Create an instance to store game statistics.
        # and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.fire_bullet = False
        self.BK = 0
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #Make the play button
        #self.play_button = Button(self, "Play")
        self.play_button = Button(self, "Press Space to Start")
        
        #self.bgx = pygame.image.load("images/bg.png")
        
        #self.bgimage = self.settings.bg_color
        #self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = 0

        self.movingUpSpeed = 1
        
        self.star_field_slow = []
        self.star_field_medium = []
        self.star_field_fast = []
        
        for slow_stars in range(50):
            self.star_loc_x = random.randrange(0, self.width)
            self.star_loc_y = random.randrange(0, self.height)
            self.star_field_slow.append([self.star_loc_x, self.star_loc_y])

        for medium_stars in range(35):
            self.star_loc_x = random.randrange(0, self.width)
            self.star_loc_y = random.randrange(0, self.height)
            self.star_field_medium.append([self.star_loc_x, self.star_loc_y])

        for fast_stars in range(15):
            self.star_loc_x = random.randrange(0, self.width)
            self.star_loc_y = random.randrange(0, self.height)
            self.star_field_fast.append([self.star_loc_x, self.star_loc_y])
            
        self.WHITE = (255, 255, 255)
        self.LIGHTGREY = (192, 192, 192)
        self.DARKGREY = (128, 128, 128)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.MAGENTA = (255, 0, 255)
        self.CYAN = (0, 255, 255)
        
        self.clock = pygame.time.Clock()
        
        self.bgm = ['sounds/play1.mp3', 'sounds/play2.mp3', 'sounds/play3.mp3']
        self.currently_playing_bgm = None
        
        self.stx = ['sounds/hit1.mp3', 'sounds/hit2.mp3', 'sounds/hit3.mp3', 'sounds/hit4.mp3', 'sounds/hit5.mp3']
        self.currently_playing_stx = None
        
        if self.stats.game_active == False:
            mixer.music.load("sounds/main_menu.mp3")
            mixer.music.set_volume(1)
            mixer.music.play(loops=-1)

    def update(self):
        self.bgY1 -= self.movingUpSpeed
        self.bgY2 -= self.movingUpSpeed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height
            
    def render(self):
        self.screen.blit(self.bgimage, (self.bgX1, self.bgY1))
        self.screen.blit(self.bgimage, (self.bgX2, self.bgY2))

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()
            
            if self.fire_bullet == True and self.BK == 0:
                self._fire_bullet()
                self.fire_bullet == False
                self.BK += 1
            
            if self.BK == 45:
                self.BK = 0
            elif self.BK > 0:
                self.BK += 1
            
            #print(self.BK)
                
            self._update_screen()
    
    def _check_events(self):
        """Respond to keypress and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.USEREVENT:
                self._play_music()

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Reset the game statitics.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            #Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            #Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            #Hide the mouse cursor
            pygame.mouse.set_visible(False)
            
            self._play_music()

    def _check_keydown_events(self,event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT and self.stats.game_active:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT and self.stats.game_active:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self.fire_bullet = True
            #self._fire_bullet()
        elif event.key == pygame.K_SPACE and self.stats.game_active == False:
            #Reset the game statitics.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            #Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            #Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            #Hide the mouse cursor
            pygame.mouse.set_visible(False)
            
            self._play_music()

    def _check_keyup_events(self,event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_SPACE:
            self.fire_bullet = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            effect = pygame.mixer.Sound('sounds/fire.mp3')
            effect.set_volume(1)
            effect.play()


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        #Remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            self._play_stx()

        if not self.aliens:
            #Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            #increase level
            self.stats.level += 1
            self.sb.prep_level()
    

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
            the update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        #Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        #    print("Ship hit!!")

        #Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()
        
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        effect = pygame.mixer.Sound('sounds/die.mp3')
        effect.set_volume(1)
        effect.play()
        if self.stats.ships_left > 0:
            #Decrement ship left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            #Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            #Pause.
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        #Create an alien and find the number of aliens in a row.
        #Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        #Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)
        #Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    def _create_alien(self, alien_number, row_number):
        #Create an alien and place it in the row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2*alien_width*alien_number
        alien.rect.x = alien.x
        alien.rect.y = (alien.rect.height + 2 * alien.rect.height * row_number) + 40
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if  alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #self.screen.fill(self.settings.bg_color)
        self.screen.fill(self.settings.bg_color)
        #self.screen.blit(self.bgx, (0, 0))
        #self.update()
        #self.render()
        
        for star in self.star_field_slow:
            star[1] += 0.5
            if star[1] > self.height:
                star[0] = random.randrange(0, self.width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(self.screen, self.DARKGREY, star, 5)

        for star in self.star_field_medium:
            star[1] += 0.75
            if star[1] > self.height:
                star[0] = random.randrange(0, self.width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(self.screen, self.LIGHTGREY, star, 2.5)

        for star in self.star_field_fast:
            star[1] += 1
            if star[1] > self.height:
                star[0] = random.randrange(0, self.width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.circle(self.screen, self.YELLOW, star, 1)
        
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #Draw the score information.
        self.sb.show_score()

        #Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()
        
        self.clock.tick(240)
    
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Treat this the same as if the ship got hit.
                self._ship_hit()
                break
            
    def _play_music(self):
        #print(pygame.mixer.music.get_busy())
        next_bgm = random.choice(self.bgm)
        while next_bgm == self.currently_playing_bgm:
            next_bgm = random.choice(self.bgm)
        self.currently_playing_bgm = next_bgm
        pygame.mixer.music.load(next_bgm)
        mixer.music.set_volume(0.5)
        pygame.mixer.music.set_endevent(pygame.USEREVENT) 
        pygame.mixer.music.play(fade_ms=1000)
        #print(pygame.mixer.music.get_busy())
        
    def _play_stx(self):
        next_stx = random.choice(self.stx)
        while next_stx == self.currently_playing_stx:
            next_stx = random.choice(self.stx)
        self.currently_playing_stx = next_stx
        effect = pygame.mixer.Sound(next_stx)
        effect.set_volume(0.75)
        effect.play()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()