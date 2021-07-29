import pygame
from pygame.sprite import Sprite

class Zombie(Sprite):
    """A class to represent a single zombie in the hoard."""

    def __init__(self, zs_game):
        """Initialize the zombie and set its starting position."""
        super().__init__()
        self.screen = zs_game.screen

        # Load the zombie image and its rect attribute.
        self.image = pygame.image.load('images/zombie.png')
        self.rect = self.image.get_rect()

        # Start each new zombie near the top right of the screen.
        self.rect.y = self.rect.height - 350
        self.rect.x = self.rect.width + 900

        # Store the zombie's exact vertical position.
        self.y = float(self.rect.y)