import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Set the dimension and properties of the button.
        #self.width, self.height = 200, 50
        '''
        Changed Play Button Shape to Rectangle 
        '''
        self.width, self.height = 600, 75
        '''
        Changed Play Button Color to Purple
        Changed Play Button Style 
        '''
        self.button_color = (255, 78, 69)
        self.text_color = (242, 166, 15)
        self.font = pygame.font.SysFont("Copperplate Gothic", 48)

        #Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #The button message needs to be prepped only once.
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)