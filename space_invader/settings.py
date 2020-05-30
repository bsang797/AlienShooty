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
        self.ship_speed = 1.5
        self.ship_proportions = 0.05