import pygame
from pygame.sprite import Sprite

class ship(Sprite):

    def __init__(self, AI_game):

        super().__init__()

        # recting the screen and setting a variable for settings

        self.screen = AI_game.screen
        self.setting = AI_game.setting
        self.screen_rect = AI_game.screen.get_rect()

        # loading an image and rescaling it

        self.image = pygame.image.load("playerShip2_orange.png")
        self.image=pygame.transform.scale(self.image,(60,38))
        self.rect = self.image.get_rect()

        # Placement

        self.rect.midbottom = self.screen_rect.midbottom

        # To tack ship

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement

        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    # Setting barriers

    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed

        if self.moving_top and self.rect.top > 400:
            self.y -= self.setting.ship_speed

        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    # Drawing the ship to the screen

    def blit(self):

        self.screen.blit(self.image, self.rect)