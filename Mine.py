from Building import *

class Mine(Building):

    def __init__(self, params):
        params.type = 'mine'
        super().__init__(params)


