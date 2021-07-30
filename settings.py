class Settings: 
    """A class to store all settings for Zombie Shooter."""

    def __init__(self):
        """Intialize the game's settings."""
        # Screen settings 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Player Settings
        self.player_limit = 3

        # Bullet Settings 
        self.bullet_width = 60
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        #zombie settings
        self.hoard_shuffle_speed = 1
        # hoard_direction of 1 represents down, -1 represents up 
        self.hoard_direction = 1

        #how quickly the game speeds up
        self.speedup_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.player_speed = 5
        self.bullet_speed = 6
        self.zombie_speed = 1.5

    def increase_speed(self):
        """Increase speed settings"""
        self.player_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.zombie_speed *= self.speedup_scale