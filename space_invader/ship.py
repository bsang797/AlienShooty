import pygame
import os

from settings import Settings

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()

        # Load the ship image and get its rect.
        os.chdir('..')
        self.image = pygame.image.load('images/bo_ship.bmp')
        self.image = pygame.transform.scale(self.image, (
            int(self.settings.screen_width/(1/self.settings.ship_proportions)),
            int((self.settings.screen_width/(1/self.settings.ship_proportions))/
                self.image.get_rect().size[0]*self.image.get_rect().size[1])))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)