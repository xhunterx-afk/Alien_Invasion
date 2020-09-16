import pygame
import sys

from time import sleep

from game_stats import Gamestats
from Settings import Settings
from ship import ship
from bullet import Bullet
from button import Button
from alien import Alien
from score_board import scoreboard

class AlienInvasion:

    # Display settings as adding alien,ship and bullets to the screen

    def __init__(self):

        pygame.init()
        self.setting = Settings()

        # Setting the screen

        self.screen=pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height

        self.background=pygame.image.load("starfield.png")

        # Setting a Caption

        pygame.display.set_caption("Alien Invasion")

        # Setting a value for other python pages that are imported

        self.stats = Gamestats(self)
        self.S_B=scoreboard(self)
        self.ship = ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.S_B.check_high_score()
        self.create_fleet()


        # Setting button and a message

        self.play_button = Button(self, "Play")

    # Runs the game/functions

    def run_game(self):

        while True:

            self.check_event()

            if self.stats.game_active:

                self.ship.update()
                self.bullets.update()
                self.update_bullet()
                self.update_alien()

            self.update_screen()

    # runs the two function key up and key down

    def check_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.Check_KEYDOWN(event)

            elif event.type == pygame.KEYUP:
                self.Check_KEYUP(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    # sees if the key is still pressed or not to continue the movement

    def Check_KEYDOWN(self, event):

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        if event.key == pygame.K_UP :
            self.ship.moving_top = True

        if event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True

        if event.key == pygame.K_SPACE:
            self._fire_bullet()

        if event.key == pygame.K_q:
            sys.exit()

    # sees if the key is still pressed or not to stop the movement

    def Check_KEYUP(self, event):

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        if event.key == pygame.K_UP:
            self.ship.moving_top = False

        if event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False

    # Fires the bullets

    def _fire_bullet(self):

        # Amount of bullets that are allowed

        if len(self.bullets) < self.setting.allowed_bullet:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    # Takes the alien and fills the screen with the alien image

    def create_fleet(self):

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        available_space_x = self.setting.screen_width - (2 * alien_width)
        number_alien_x = available_space_x//(2*alien_width)

        ship_height = self.ship.rect.height

        available_space_y = (self.setting.screen_height-(5*alien_height)-ship_height)
        number_alien_y = available_space_y // (2*alien_height)

        for row_number in range(number_alien_y):
            for alien_number in range(number_alien_x):

                self.create_alien(alien_number, row_number)

    # Creates an alien

    def create_alien(self, alien_number, row_number):

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x

        alien.rect.y = alien.rect.height+2*alien.rect.height*row_number

        self.aliens.add(alien)

    # Checks if the fleet (the alien) have hit the edge or not

    def check_fleet_edges(self):

        # check if alien hit the edge

        for alien in self.aliens.sprites():
            if alien.check_edge():
                self.change_fleet_direction()
                break

    # Changing direction of the aliens

    def change_fleet_direction(self):

        # change the fleet direction and drops the alien

        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed

        self.setting.fleet_direction *= -1

    def check_play_button(self,mouse_pos):

        button_clicked=self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:

            self.setting.initialize_dynamic_settings()

            self.stats.reset_stats()

            self.stats.game_active=True
            self.S_B.prep_score()

            self.aliens.empty()
            self.bullets.empty()

            self.create_fleet()
            self.ship.center_ship()
            self.S_B.prep_ship()

            # mouse unvisible

            pygame.mouse.set_visible(False)
    # If ship gets hit by alien

    def ship_hit(self):

        if self.stats.ships_left > 0:

            # Removes a life of a player

            self.stats.ships_left -= 1
            self.S_B.prep_ship()

            # Removes bullets and aliens fleets

            self.aliens.empty()
            self.bullets.empty()

            # recenter the ship and recreate a fleet

            self.create_fleet()
            self.ship.center_ship()

            # Pause

            sleep(0.5)

        else:

            self.stats.game_active = False

            # Mouse visible

            pygame.mouse.set_visible(True)

    def check_alien_bottom(self):

        # Makes the screen a rectangle

        screen_rect = self.screen.get_rect()

        # Checks if the alien ship have hit the bottom screen

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    # Removing the bullets and checking for a collision between alien and bullet

    def update_bullet(self):

        # Removes the bullet if goes throw the top if the display

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.check_bullet_hit()
        # Collision to see if the bullets have hit the alien ship

    def check_bullet_hit(self):

        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # Adding points

        if collision:
            self.stats.score += self.setting.alien_points
            self.S_B.prep_score()
            self.S_B.check_high_score()

        # Repopulating and Increasing speed

        if not self.aliens:

            self.bullets.empty()
            self.create_fleet()
            self.setting.increase_speed()

    # Running two function that moves and checks if the alien hit the edges

    def update_alien(self):

        # Runs two functions the first one moves the fleet of alien and the second checks if the alien have hit and edge

        self.aliens.update()
        self.check_fleet_edges()

        # Runs an if function to check for a collide between ship and alien

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()

        # Runs a function that checks if the alien have hit the bottom of the screen

        self.check_alien_bottom()

    # filling the screen and drawing bullets

    def update_screen(self):

        # Fills the screen with a background

        self.screen.blit(self.background, (0,0))

        # Display the Ship

        self.ship.blit()

        # Draw bullets on the screen

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw alien to the display

        self.aliens.draw(self.screen)

        self.S_B.show_score()
        self.S_B.check_high_score()

        # Play Button

        if not self.stats.game_active:
            self.play_button.draw_button()

        # display flip

        pygame.display.flip()


if __name__ == '__main__':
    AI = AlienInvasion()
    AI.run_game()