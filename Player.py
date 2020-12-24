class Player:
    def __init__(self, params):
        self.Baza = None

        self.user_name = params['user_name']       # выводится на экран
        self.number = params['number']
        #self.color = params['color']

    def addBaza(self, Baza):
        if self.Baza is not None:
            print('Player addBaza. self.Baza is not None')

        self.Baza = Baza

