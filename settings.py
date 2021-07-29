class Settings: 
    """A class to store all settings for Zombie Shooter."""

    def __init__(self):
        """Intialize the game's settings."""
        # Screen settings 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Player Settings
        self.player_speed = 1.5

        # Bullet Settings 
        self.bullet_speed = 1.0 
        self.bullet_width = 28
        self.bullet_height = 9
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        