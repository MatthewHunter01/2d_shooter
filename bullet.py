import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the player"""

    def __init__(self, zs_game):
        """Create a bullet object at the players current position."""
        super().__init__()
        self.screen = zs_game.screen
        self.settings = zs_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midleft = zs_game.player.rect.midleft

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen."""
        # Update the decimal position of the bullet 
        self.x -= self.settings.bullet_speed
        # Update the rect positon. 
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)