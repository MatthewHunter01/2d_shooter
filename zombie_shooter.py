import sys 

import pygame

class ZombieShooter:
    """Overall class to manage game assets and behavior"""

    def __init__(self) -> None:
        """Initilize the game and create game resouces"""
    pygame.init()

    self.screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("ZombieShooter")

    def run_game(self): 
        """Start the main loop for the game."""
        while True: 
            # Watch for keyboard and mouse event.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    zs = ZombieShooter()
    zs.run_game()

