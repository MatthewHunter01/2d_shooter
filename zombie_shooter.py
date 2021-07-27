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

        self.player = Player(self)

    def run_game(self): 
        """Start the main loop for the game."""
        while True: 
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Move the player up.
                    self.player.rect.y -= 1
                    

    def _update_screen(self):               
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    zs = ZombieShooter()
    zs.run_game()

