import pygame
from pygame.sprite import Sprite

class Settings:
    """A Class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        self.screen_width = 1280 #960
        self.screen_height = 720 #720
        self.bg_color = (15, 15, 15) #(230, 230, 230)
        #self.bg_color = pygame.image.load('images/ship3.bmp')

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Bullet settings
        '''
        Changed Bullet Speed from 1.5 to 10
        '''
        self.bullet_speed = 3
        '''
        Changed Bullet Width from 3 to 2
        Changed Bullet Height from 15 to 10
        '''
        self.bullet_width = 2
        self.bullet_height = 17.5
        self.bullet_color = (192,192,192) #(255, 255, 255)
        '''
        Changed Self Bullet Allowed from 3 to 15
        '''
        self.bullets_allowed = 100

        #Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 7.5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #How quickly the game speeds up
        self.speedup_scale = 1.05

        #How quickly the alien point values increase
        self.score_scale = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2 #1.5
        self.bullet_speed = 10 #3.0
        self.alien_speed = 1  #0.5

        #fleet_direction of 1 represents right, -1 represents left.
        '''
        Changed Alien First Move to Left
        '''
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 1 #50
    
    def increase_speed(self):
        """Increase speed settings and aliens point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)