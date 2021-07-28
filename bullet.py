import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the player"""

    def __init__(self, zs_game):
        """Create a bullet object at the players current position."""
        super().__init__()
        self.sceen = zs_game.screen
        self.settings = zs_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midright = zs_game.player.rect.midright

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)