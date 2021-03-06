import pygame
from pygame.sprite import Sprite

class R_Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.ship = ai_game.ship
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) then set correct position
        self.image = pygame.image.load('images/annoy_bullet.bmp')
        self.image = pygame.transform.scale(
            self.image, (self.settings.bullet_width, self.settings.bullet_height))

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.rect.x += self.ship.ship_width/3.8

        # Store the bullet's position as a decimal value
        self.y  = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        self.screen.blit(self.image, self.rect)