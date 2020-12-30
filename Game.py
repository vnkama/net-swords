import pygame as pg
import numpy as np
from config import *
from functions import *

from Tile import *
from Mine import *
from Base import *
from Player import *



class Game:

    def __init__(self):

        self.Players = []
        self.Units = []
        self.Bases = []
        self.Tiles = np.empty([MAP_SIZE_X, MAP_SIZE_Y], dtype=object)
        self.Mines =[]

        self.pg_group_buildings = pg.sprite.Group()

        self.map_rect = pg.Rect(0, 0, TILE_SIZE * MAP_SIZE_X, TILE_SIZE * MAP_SIZE_Y)

        # генерируем тайлы
        for i, v in np.ndenumerate(self.Tiles):
            self.Tiles[i] = Tile(i)

        self.game_tick = 0

        self.rnd_gen = np.random.default_rng()

        self.Players.append(
                Player({
                    'user_name': 'Name bottom',
                    'player_number': 1,
                    'color': PLAYER_1_CLR,
                    'start_pos': 'bottom',
                    'rnd_gen': self.rnd_gen,
                    'game': self,
                })
        )

        self.Players.append(
                Player({
                    'user_name': 'Name top',
                    'player_number': 2,
                    'color': PLAYER_2_CLR,
                    'start_pos': 'top',
                    'rnd_gen': self.rnd_gen,
                    'game': self,

                })
        )

        self.createMines()

        self.debugTestRadius()

    def debugTestRadius(self):
        CENTR = (20,20)

        self.Tiles[CENTR].red = True
        instr = ''
        cnt = 0

        for x in range(-15,15):
            for y in range(-15, 15):
                if calcDistancePoint1((x,y)) == 10:
                    self.Tiles[CENTR[0] + x, CENTR[1]+y].green = True
                    instr += f'[{x},{y}],'
                    cnt += 1
                    if cnt == 10:
                        print(instr)
                        instr = ''
                        cnt = 0

        if len(instr):
            print(instr)



    def addBase(self,p_num, new_base):
        #new_base = self.Players[p_num].addBase()

        self.Tiles[new_base.coord].setBuilding(new_base)
        self.Bases.append(new_base)


    # генерируем шахты
    def createMines(self):

        q1x = 0
        q1y = 0
        q2x = int(MAP_SIZE_X/2)
        q2y = int(MAP_SIZE_Y/2)
        q3x = int(MAP_SIZE_X)
        q3y = int(MAP_SIZE_Y)

        # поле квадратное генерим по одной шахет в каждой четверти (квадранте)

        # зоны в которых генируем шахты
        Zones = []
        Zones.append([q1x, q2x, q1y, q2y])      # 1й квадрант
        Zones.append([q2x, q3x, q1y, q2y])      # 2й квадрант
        Zones.append([q1x, q2x, q2y, q3y])      # 3й квадрант
        Zones.append([q2x, q3x, q2y, q3y])      # 4й квадрант

        # генерим еще по 3 шахты на каждой половине поля
        Zones.append([q1x, q3x, q1y, q2y])      # 1я половина
        Zones.append([q1x, q3x, q2y, q3y])      # 2я половина

        Zones.append([q1x, q3x, q1y, q2y])      # 1я половина
        Zones.append([q1x, q3x, q2y, q3y])      # 2я половина

        Zones.append([q1x, q3x, q1y, q2y])      # 1я половина
        Zones.append([q1x, q3x, q2y, q3y])      # 2я половина

        Bases = []
        Bases.append(self.Players[0].Base.coord)
        Bases.append(self.Players[1].Base.coord)

        # генерируем
        mines_coords = []

        for zone in Zones:
            loop = True
            new_coord = None
            while loop:
                # генерируем точку
                x = self.rnd_gen.integers(zone[0], zone[1])
                y = self.rnd_gen.integers(zone[2], zone[3])
                new_coord = (x,y)
                loop=False

                # проверим новую точку на колллизии с предыдущими шахтами
                if len(mines_coords):
                    for cur_coords in mines_coords:
                        if calcDistancePoints2(new_coord, cur_coords) < 7:
                            loop = True
                            break

                # проверим на коллизии с базами
                if not loop:
                    for cur_coords in Bases:
                        if calcDistancePoints2(new_coord, cur_coords) < 10:
                            loop = True
                            break


            # координата готова, сохраним
            mines_coords.append(new_coord)

        for cur_coord in mines_coords:

            new_mine = Mine({
                'player_num': 0,
                'coord': cur_coord,
                'player_color': None,
                'sprite_groups':(self.pg_group_buildings),
            })

            self.Tiles[cur_coord].setBuilding(new_mine)
            self.Mines.append(new_mine)

    def update(self):
        pass

    def draw(self, surface):

        surface.fill(MAP_BACKGROUND_CLR, self.map_rect)

        for i, v in np.ndenumerate(self.Tiles):
            self.Tiles[i].draw_1(surface)

        self.pg_group_buildings.draw(surface)

    #
    # ищет ближайший свободный тайл
    #
    def findNearFreeTail(self, coord):
        if self.Tiles:
            pass







