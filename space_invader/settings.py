class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1345
        self.screen_height = 1010
        self.bg_color = (230, 230, 230)
        self.fullscreen = False
        self.greece_background = True

        # Window position settings
        self.window_x = 0
        self.window_y = 30

        # Ship setting
        self.ship_speed = 12.0
        self.ship_proportions = 0.1

        # Bullet settings
        self.bullet_speed = 4.0
        self.bullet_width = 6
        self.bullet_height = 30
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 20

        # Alien settings
        self.alien_proportions = 0.05
        self.alien_rand_position = True
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1