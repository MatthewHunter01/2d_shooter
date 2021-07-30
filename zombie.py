from settings import Settings
import pygame
from pygame.sprite import Sprite

class Zombie(Sprite):
    """A class to represent a single zombie in the hoard."""

    def __init__(self, zs_game):
        """Initialize the zombie and set its starting position."""
        super().__init__()
        self.screen = zs_game.screen
        self.settings = zs_game.settings

        self.image = pygame.image.load('images/zombie.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height
        

        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if zombie is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= 0 or self.rect.top <= screen_rect.top: 
            return True

    def update(self):
        """Move the zombies up or down"""
        self.y += (self.settings.zombie_speed * 
                        self.settings.hoard_direction)
        self.rect.y = self.y

    