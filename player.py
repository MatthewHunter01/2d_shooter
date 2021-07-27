import pygame

class Player:
    def __init__(self, zs_game):
        """Initialize the player and set its starting position"""
        self.screen = zs_game.screen
        self.screen_rect = zs_game.screen.get_rect()

        # Load the player image and get its rect.
        self.image = pygame.image.load('images/player.bmp')
        self.rect = self.image.get_rect()
        # Start each new player at the left center of the screen/
        self.rect.midleft = self.screen_rect.midleft 
        """Initialize the player and set its starting position"""
        self.screen = zs_game.screen
        self.screen_rect = zs_game.screen.get_rect()

        # Load the player image and get its rect.
        self.image = pygame.image.load('images/player.bmp')
        self.rect = self.image.get_rect()
        # Start each new player at the left center of the screen/
        self.rect.midleft = self.screen_rect.midleft 

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the players position based on the movement flags."""
        if self.moving_up: 
            self.rect.y -= 1
        if self.moving_down: 
            self.rect.y += 1

    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)