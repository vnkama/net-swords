import pygame as pg

class Building(pg.sprite.Sprite):


    def __init__(self, params):

        super().__init__(params['sprite_groups'])

        self.type = params['type']
        self.player_num = params['player_num']
        self.coord = params['coord']
        self.player_color = params['player_color']

        if params.get('select_color', False):
            self.image = self.image_red

        self.rect = None


    def setRect(self,rect):
        self.rect = rect



