from _typeshed import Self
import sys 

import pygame

from settings import Settings
from player import Player

class ZombieShooter:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initilize the game and create game resouces"""
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Zombie Shooter")

        self.player = Player(Self)

    def run_game(self): 
        """Start the main loop for the game."""
        while True: 
            # Watch for keyboard and mouse event.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)
            self.player.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    zs = ZombieShooter()
    zs.run_game()

