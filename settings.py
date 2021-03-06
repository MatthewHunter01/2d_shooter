class Settings: 
    """A class to store all settings for Zombie Shooter."""

    def __init__(self):
        """Intialize the game's settings."""
        
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

       
        self.player_limit = 3

        
        self.bullet_width = 60
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        
        self.hoard_shuffle_speed = 1
        
        self.hoard_direction = 1

        
        self.speedup_scale = 1.5
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.player_speed = 5
        self.bullet_speed = 6
        self.zombie_speed = 1.5

        self.zombie_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.player_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.zombie_speed *= self.speedup_scale

        self.zombie_points = int(self.zombie_points * self.score_scale)
        print(self.zombie_points)