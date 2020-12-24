from Building import *

class Baza(Building):

    def __init__(self, params):
        params['type'] = 'baza'
        super().__init__(params)

    def draw(self, surface, rect):
        pass
        #rect()


