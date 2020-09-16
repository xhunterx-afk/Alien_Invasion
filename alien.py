import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,AI_game):

        super().__init__()

        self.screen = AI_game.screen
        self.settings = AI_game.setting

        # loading an image and resizing it

        self.image = pygame.image.load("alien2.bmp")
        self.image=pygame.transform.scale(self.image,(70,70))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    # checking for the edge of the scree

    def check_edge(self):

        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True

        elif self.rect.left <= 0:
            return True

    def update(self):

        # moving the alien

        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)

        self.rect.x = self.x