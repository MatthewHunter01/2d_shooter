import pygame

class Player:
    def __init__(self, zs_game):
        """Initialize the player and set its starting position"""
        self.screen = zs_game.screen
        self.settings = zs_game.settings
        self.screen_rect = zs_game.screen.get_rect()

        # Load the player image and get its rect.
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        # Start each new player at the left center of the screen/
        self.rect.midleft = self.screen_rect.midleft 
        """Initialize the player and set its starting position"""
        self.screen = zs_game.screen
        self.screen_rect = zs_game.screen.get_rect()

        # Load the player image and get its rect.
        self.image = pygame.image.load('images/player.png')
        self.rect = self.image.get_rect()
        # Start each new player at the left center of the screen/
        self.rect.midleft = self.screen_rect.midleft 

        # Store a decimal value for the players vertical position.
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the players position based on the movement flags."""
        # Update the players y value, not the rect.
        if self.moving_up and self.rect.top > 0: 
            self.y -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: 
            self.y += self.settings.player_speed

        # Update rect object from self.y.
        self.rect.y = self.y

    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)