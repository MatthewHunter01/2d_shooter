import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, zs_game):
        """Initialize the player and set its starting position"""
        super().__init__()
        self.screen = zs_game.screen
        self.settings = zs_game.settings
        self.screen_rect = zs_game.screen.get_rect()

        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.rect.midright = self.screen_rect.midright 
        """Initialize the player and set its starting position"""
        self.screen = zs_game.screen
        self.screen_rect = zs_game.screen.get_rect()

        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        self.rect.midright = self.screen_rect.midright 

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the players position based on the movement flags."""
        if self.moving_up and self.rect.top > 0: 
            self.y -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: 
            self.y += self.settings.player_speed

        self.rect.y = self.y

    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_player(self):
        """Center the ship on the screen"""
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)