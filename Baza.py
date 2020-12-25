import pygame as pg
from Building import *

class Baza(Building):

    def __init__(self, params):
        params['type'] = 'baza'
        super().__init__(params)

    def draw(self, surface, rect):
        pg.draw.rect(surface, self.player_color, rect)



