import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, AI_game):

        super().__init__()
        self.screen = AI_game.screen
        self.setting = AI_game.setting

        # Loading an image

        self.image=pygame.image.load("laserRed01.png").convert_alpha()
        self.image_rect=self.image.get_rect()

        # Bullet start line

        self.rect = self.image_rect
        self.rect.midbottom = AI_game.ship.rect.midtop

        self.y = float(self.rect.y)


    def update(self):

        # Direction of the bullet

        self.y -= self.setting.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):

        self.screen.blit(self.image, self.rect)
