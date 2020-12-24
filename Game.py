import pygame as pg
import numpy as np
from config import *
from Tile import *


class Game:

    def __init__(self):


        self.Tiles = np.empty([MAP_SIZE_X_TILE, MAP_SIZE_Y_TILE], dtype=object)

        for i, v in np.ndenumerate(self.Tiles):
            self.Tiles[i] = Tile(i)


        self.Baza1 = {
            'coord': (48,25)
        }

        self.Tiles[48][25].setBuilding(self.Baza1)


    def update(self):
        pass

    def draw(self, surface):


        for i, v in np.ndenumerate(self.Tiles):
            self.Tiles[i].draw(surface)











