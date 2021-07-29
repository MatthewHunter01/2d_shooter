import sys 

import pygame

from settings import Settings
from player import Player
from bullet import Bullet
from zombie import Zombie

class ZombieShooter:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initilize the game and create game resouces"""
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Zombie Shooter")

        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()

        self._create_hoard()

    def run_game(self): 
        """Start the main loop for the game."""
        while True: 
            self._check_events()
            self.player.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to key press """
        if event.key == pygame.K_UP:
                    self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
                    self.player.moving_down =True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
                    self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
                    self.player.moving_down = False

    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy(): 
            if bullet.rect.left > 2000:
                self.bullets.remove(bullet)

    def _create_hoard(self):
        """Create the hoard of zombies."""
        # create a zombie and find a number of zombies in a row
        # Spacing between each zombie is equal to one zombie height
        zombie = Zombie(self)
        zombie_height = zombie.rect.height
        availble_space_y = self.settings.screen_height - (2 * zombie_height)
        number_zombies_y = availble_space_y // (2 * zombie_height)

        #create the first row of zombies 
        for zombie_number in range(number_zombies_y):
            #create a zombie and place it in the row.
            zombie = Zombie(self)
            zombie.y = zombie_height + 2 * zombie_height * zombie_number
            zombie.rect.y = zombie.y
            self.zombies.add(zombie)
                    

    def _update_screen(self):               
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.zombies.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    zs = ZombieShooter()
    zs.run_game()

