x = 0
y = 30
import os
import sys
import pygame

from settings import Settings
from ship import Ship
from l_bullet import L_Bullet
from r_bullet import R_Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Set position of display window to top left corner
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (
            self.settings.window_x, self.settings.window_y)

        if self.settings.fullscreen:
            # Open display window in fullscreen mode
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            # Open display window in windowed mode
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width,self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Load background image
        # self.background = pygame.image.load('images/greece.bmp')

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Get rid of bullets that are off screen.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

            self._update_screen()

    def _check_events(self):
        """Responds to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responds to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responds to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_l_bullet = L_Bullet(self)
        new_r_bullet = R_Bullet(self)
        self.bullets.add(new_l_bullet)
        self.bullets.add(new_r_bullet)

    def _update_screen(self):
        """Updates images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        # self.screen.blit(self.background, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

if  __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
