import pygame as pg
from Building import *

class Base(Building):

    image_red = pg.image.load("./img/flag-red-16.png").convert_alpha()
    image_blue = pg.image.load("./img/flag-blue-16.png").convert_alpha()

    def __init__(self, params):
        self.image = None

        params['type'] = 'base'
        params['select_color'] = True

        super().__init__(params)

        if self.player_num == 1:
            self.image = Base.image_red
        elif self.player_num == 2:
            self.image = Base.image_blue




