class GameStats:
    """Track stats for Zombie Shooter"""
    

    def __init__(self, zs_game):
        """Initialize stats"""
        self.settings = zs_game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        """Initialize stats that can change during the game."""
        self.players_left = self.settings.player_limit
        self.score = 0 