import sys 

import pygame

from settings import Settings

class ZombieShooter:
    """Overall class to manage game assets and behavior"""

    def __init__(self) -> None:
        """Initilize the game and create game resouces"""
    pygame.init()
    self.settings = Settings()


    self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Zombie Shooter")

    # Set the background color .
    self.bg_color = (230, 230, 230)

    def run_game(self): 
        """Start the main loop for the game."""
        while True: 
            # Watch for keyboard and mouse event.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    zs = ZombieShooter()
    zs.run_game()

