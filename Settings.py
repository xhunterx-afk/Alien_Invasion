
class Settings:

    def __init__(self):

        # SCREEN Settings

        self.screen_width=1280
        self.screen_height=800


        # BULLET Setting

        self.bullet_height=10
        self.bullet_width=3
        self.allowed_bullet=6


        # ALIEN Settings

        self.fleet_drop_speed=15

        # Ship

        self.ship_limit=3

        self.speedup_scale=1.1

        self.score_scale=1.5

        self.initialize_dynamic_settings()

    # Movements speed

    def initialize_dynamic_settings(self):

        self.ship_speed = 5.5
        self.bullet_speed = 5.5
        self.alien_speed = 20.0

        self.fleet_direction=1

        self.alien_points = 50

    # Incremental of the speed for the objects

    def increase_speed(self):

        self.ship_speed *=  self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points=int(self.alien_points * self.score_scale)
