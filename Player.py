import numpy as np
from config import *
from Base import *

class Player:
    def __init__(self, params):
        self.Base = None
        self.user_name = None
        self.player_number = None
        self.keyword = None

        self.is_client_registered = False

        #self.user_name = params['user_name']       # выводится на экран

        self.player_number = params['player_number']
        self.color = params['color']
        self.start_pos = params['start_pos']

        self.rnd_gen = params['rnd_gen']
        self.game = params['game']

        self.addBase()



    def registerClient(self, user_name):
        if self.is_client_registered:
            # клиент уже зарегистрирован
            return False
        else:
            # регистрируем нового клиента
            if len(user_name) < 3 or len(user_name) < 20:
                return False

            self.user_name = user_name

            # генерим случайную строку вида "5673834657"
            self.keyword = str(self.rnd_gen.integers(0,10,10))

            self.is_client_registered = True

            return self.keyword



    # генерим базу, сообщаем в игру
    def addBase(self):
        x_zone_size = int(MAP_SIZE_X / 2)
        y_zone_size = int(MAP_SIZE_Y / 15)

        base_x = int((MAP_SIZE_X - x_zone_size)/2 + self.rnd_gen.integers(0,x_zone_size))

        y_offs =  0 if (self.start_pos == 'top') else (MAP_SIZE_Y - y_zone_size)
        base_y = y_offs + self.rnd_gen.integers(0, y_zone_size)

        self.Base = Base({
            'player_num': self.player_number,
            'coord': (base_x, base_y),
            'player_color': self.color,
            'sprite_groups': (self.game.pg_group_buildings),
        })

        self.game.addBase(self.player_number, self.Base)





