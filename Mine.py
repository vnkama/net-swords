import pygame as pg
from config import *
from Building import *

class Mine(Building):

    image_red = pg.image.load("./img/mine-red-16.png").convert_alpha()
    image_blue = pg.image.load("./img/mine-blue-16.png").convert_alpha()
    image_black = pg.image.load("./img/mine-grey-16.png").convert_alpha()


    def __init__(self, params):
        params['type'] = 'mine'

        super().__init__(params)

        if self.player_num == 1:
            self.image = Mine.image_red
        elif self.player_num == 2:
            self.image = Mine.image_blue
        else:
            self.image = Mine.image_black



    # def draw(self, surface, rect):
    #     if not self.player_color:
    #         #pg.draw.rect(surface, THEME_LIGHT_GREY_CLR, rect)
    #         #self.rect = rect
    #         pg.draw(surface)
    #     else:
    #         pg.draw.rect(surface, self.player_color, rect)




