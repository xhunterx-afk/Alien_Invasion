import pygame.font
from pygame.sprite import Group
from ship import ship as Ships

class scoreboard:

    def __init__(self, AI_game):

        # Defining functions

        self.AI_game = AI_game
        self.screen = AI_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = AI_game.setting
        self.stats = AI_game.stats

        # Setting a color text and and Size

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 38)

        # Running the functions

        self.prep_score()
        self.high_score()
        self.prep_ship()

    def prep_score(self):

        # Rounding the numbers to give cleaner number

        rounded_score=round(self.stats.score, -1)
        score_str="{:,}".format(rounded_score)

        # Transforming text to an image

        self.score_image = self.font.render(score_str, True, self.text_color)

        # recting the text/image and positioning it

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def high_score(self):

        # Rounding the numbers to give cleaner number

        high_score = round(self.stats.score, -1)
        high_score_str = "{:,}".format(high_score)

        # Transforming text to an image


        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # recting the text/image and positioning it

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_ship(self):

        # Defining ship as a group

        self.ships=Group()

        # Adding as most ships as the player life's

        for ship_number in range(self.stats.ships_left):

            ship=Ships(self.AI_game)
            ship.rect.x = 10+ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def check_high_score(self):

        # replacing/ Making a new high score

        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.high_score()
            with open("Highscore.txt","w") as f:
                f.write(str(self.stats.score))


    def show_score(self):

        # Drawing images

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)