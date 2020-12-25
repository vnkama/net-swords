import pygame as pg
import numpy as np
from config import *

from Tile import *
from Mine import *
from Baza import *
from Player import *



class Game:

    def __init__(self):

        self.map_rect = pg.Rect(0, 0, TILE_SIZE * MAP_SIZE_X_TILE, TILE_SIZE * MAP_SIZE_Y_TILE)

        self.Tiles = np.empty([MAP_SIZE_X_TILE, MAP_SIZE_Y_TILE], dtype=object)
        self.Buldings = []

        for i, v in np.ndenumerate(self.Tiles):
            self.Tiles[i] = Tile(i)

        self.game_tick = 0

        #==============
        self.Player1 = Player({
            'user_name': 'Nicolas',
            'number': 1,
            'color': PLAYER_1_CLR,
        })

        self.Player2 = Player({
            'user_name': 'antibot',
            'number': 2,
            'color': PLAYER_2_CLR,
        })

        #==============

        bld = Baza({
            'player': 1,
            'coord': (25, 48),
            'player_color': self.Player1.color
        })

        self.Tiles[bld.coord].setBuilding(bld)
        self.Buldings.append(bld)
        self.Player1.addBaza(bld)

        #==============

        bld = Baza({
            'player': 2,
            'coord': (35, 1),
            'player_color': self.Player2.color
        })

        self.Tiles[bld.coord].setBuilding(bld)
        self.Buldings.append(bld)
        self.Player2.addBaza(bld)


        #==============



    def update(self):
        pass

    def draw(self, surface):

        surface.fill(MAP_BACKGROUND_CLR, self.map_rect)

        for i, v in np.ndenumerate(self.Tiles):
            self.Tiles[i].draw(surface)











