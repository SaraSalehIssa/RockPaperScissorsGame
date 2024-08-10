from Player import Player


class CyclePlayer(Player):
    def __init__(self):
        self.moves = ['rock', 'paper', 'scissors']
        self.index = 0

    def choice(self):
        choice = self.moves[self.index]
        self.index = (self.index + 1) % 3
        return choice
