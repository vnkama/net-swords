import pygame as pg
from config import *

import numpy as np


class Tile:

    def __init__(self, coord):
        self.Units = []
        self.Building = None
        self.coord = coord

        self.rect = pg.Rect(coord[0]*TILE_SIZE, coord[1]*TILE_SIZE, TILE_SIZE, TILE_SIZE)

        if (coord[0] + coord[1]) % 2 == 0:
            self.background_color = THEME_MED_GREY_CLR
        else:
            self.background_color = THEME_DARK_GREY_CLR



    def addUnit(self, unit):
        self.Units.append(unit)

    def addUnits(self,units_arr):
        self.Units.append(units_arr)

    def delUnit(self, unit):
        try:
            self.Units.remove(unit)
        except ValueError:
            pass


    def getUnitsCount(self):
        return len(self.Units)

    def getBuilding(self):
        return self.Building

    def setBuilding(self, building):
        self.Building = building

    def draw(self, surface):
        pg.draw.rect(surface, MAP_NET_CLR, pg.Rect(self.rect.topleft,(2,2)))

        if self.Building is not None:
            self.Building.draw(surface, self.rect)

