class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 490
        self.bg_color = (230, 230, 230)
        self.fullscreen = True

        # Window position settings
        self.window_x = 0
        self.window_y = 30

        # Ship setting
        self.ship_speed = 6
        self.ship_proportions = 0.05

        # Bullet settings
        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6