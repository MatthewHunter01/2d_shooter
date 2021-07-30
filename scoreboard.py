import pygame.font
from pygame.sprite import Group

from player import Player

class Scoreboard:
    """A class to repor scoring information."""

    def __init__(self, zs_game):
        """Initiliaze scorekeeping attributed."""
        self.zs_game = zs_game
        self.screen = zs_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = zs_game.settings
        self.stats = zs_game.stats

        self.text_color = (30, 30 ,30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_players()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 20 

    def prep_players(self):
        """Show how many players are left."""
        self.players = Group()
        for player_number in range(self.stats.players_left):
            player = Player(self.zs_game)
            player.rect.x = 10 + player_number * player.rect.width
            player.rect.y = 10
            self.players.add(player)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.players.draw(self.screen)