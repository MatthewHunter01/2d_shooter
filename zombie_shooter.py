import sys 
from time import sleep 

import pygame
from pygame.constants import FULLSCREEN

from settings import Settings
from game_stats import GameStats
from button import Button
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

        self.stats = GameStats(self)

        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()

        self._create_hoard()

        self.play_button = Button(self, "Play")

    def run_game(self): 
        """Start the main loop for the game."""
        while True: 
            self._check_events()

            if self.stats.game_active:
                self.player.update()
                self._update_bullets()
                self._update_zombies()

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
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when button is cliked"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True

            self.zombies.empty()
            self.bullets.empty()

            self._create_hoard()
            self.player.center_player()
            pygame.mouse.set_visible(False)


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
        self.bullets.update()

        for bullet in self.bullets.copy(): 
            if bullet.rect.right <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_zombie_collisions()

    def _check_bullet_zombie_collisions(self): 
        """Respond to bullet-zombie collisions."""   
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.zombies, True, True)

        if not self.zombies:
            self.bullets.empty()
            self._create_hoard()    
            self.settings.increase_speed()

    
    def _update_zombies(self):
        """update the positions of all the zombies in the hoard."""
        self._check_hoard_edges()
        self.zombies.update()

        if pygame.sprite.spritecollideany(self.player, self.zombies):
            self._player_hit()

        #look for zombies hitting the right of the screen 
        self._check_zombies_right()

    def _player_hit(self):
        """Respond to the player being hit by a zombie."""
        if self.stats.players_left > 0:

            self.stats.players_left -= 1

            self.zombies.empty()
            self.bullets.empty()

            self._create_hoard()
            self.player.center_player()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_zombies_right(self):
        """Check if any zombies have reached the right of the screen."""
        screen_rect = self.screen.get_rect()
        for zombie in self.zombies.sprites():
            if zombie.rect.right >= screen_rect.right:
                #treat this the same as if the player got hit
                self._player_hit()
                break

    def _create_hoard(self):
        """Create the hoard of zombies."""
        zombie = Zombie(self)
        zombie_width, zombie_height = zombie.rect.size
        zombie_height = zombie.rect.height
        availble_space_y = self.settings.screen_height - (2 * zombie_height)
        number_zombies_y = availble_space_y // (2 * zombie_height)

        player_width = self.player.rect.width
        availble_space_x = (self.settings.screen_height - (
                                3 * zombie_width) - player_width)
        number_rows = availble_space_x // (2 * zombie_width)

        for row_number in range (number_rows):
            for zombie_number in range(number_zombies_y):
                self._create_zombie(zombie_number, row_number)

    def _create_zombie(self, zombie_number, row_number):
        zombie = Zombie(self)
        zombie_width, zombie_height = zombie.rect.size
        zombie_height = zombie.rect.height
        zombie.y = zombie_height + 2 * zombie_height * zombie_number
        zombie.rect.y = zombie.y
        zombie.rect.x = zombie_width + 2 * zombie.rect.width * row_number
        self.zombies.add(zombie)

    def _check_hoard_edges(self):
        """Respond appropriatly if any zombies have reached an edge."""
        for zombie in self.zombies.sprites():
            if zombie.check_edges():
                self._change_hoard_direction()
                break

    def _change_hoard_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for zombie in self.zombies.sprites():
            zombie.rect.x += self.settings.hoard_shuffle_speed
        self.settings.hoard_direction *= -1
                    

    def _update_screen(self):               
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.zombies.draw(self.screen)

        if not self.stats.game_active: 
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    zs = ZombieShooter()
    zs.run_game()

