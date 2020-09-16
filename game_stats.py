class Gamestats:

    def __init__(self,AI_game):

        self.game_active = False
        self.settings=AI_game.setting
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score =0
