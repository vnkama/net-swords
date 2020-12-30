#import pygame as pg
#import numpy as np
#from config import *
#from functions import *

from Unit import *

class Knight(Unit):

    image_red = pg.image.load("./img/knight-red-16.png").convert_alpha()
    image_blue = pg.image.load("./img/knight-blue-16.png").convert_alpha()

    HP_MAX = 100
    see_radius = 6
    attack_radius = 1
    attack_level = 15
    COST = 90
    SPEED = KNIGHT_SPEED   # tile / sec,

    MOVE_TICKS_F = int(UPDATE_FPS / SPEED)
    MOVE_TICKS_D = int(UPDATE_FPS / SPEED * 1.4142)

    def __init__(self, params):
        params['type'] = 'knight'



        super().__init__(params)

        if self.player_num == 1:
            self.image = Knight.image_red
        elif self.player_num == 2:
            self.image = Knight.image_blue

        self.hp = Knight.HP_MAX
