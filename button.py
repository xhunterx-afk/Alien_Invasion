import pygame.font

class Button:

    def __init__(self,AI_game ,msg):

        self.screen=AI_game.screen
        self.screen_rect=AI_game.screen.get_rect()

        self.width,self.height=200,50
        self.button_color=(0,0,0)
        self.text_color=(255,255,255)

        self.font=pygame.font.SysFont(None,48)

        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self,msg):

        self.msg_imgae = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_imgae_rect= self.msg_imgae.get_rect()
        self.msg_imgae_rect.center=self.rect.center

    def draw_button(self):

        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_imgae,self.msg_imgae_rect)