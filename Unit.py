import pygame as pg
#import numpy as np
#from config import *
#from functions import *

UN_ORDER_STAND = 1  # стоять там где находится
UN_ORDER_MOVE = 2
UN_ORDER_ATTACK = 3

class Unit(pg.sprite.Sprite):

    def __init(self, params):
        super().__init__(params['sprite_groups'])

        self.type = params['type']                  # ex: 'archer'
        self.player_num = params['player_num']      # 1-based
        # self.player_color = params['player_color']  # rgb

        self.coord = None                # (1,4)

        self.order = UN_ORDER_STAND
        self.order_dest = None


        self.miniorder = UN_ORDER_STAND
        self.miniorder_dest = None     # координаты клетки в которую осуществляется переход или выстрел
        self.miniorder_counter = 0      # обратынй отсчет для текущей операции


    def setOrder(self, order, coord = None):
        self.order = order
        self.order_dest = coord


