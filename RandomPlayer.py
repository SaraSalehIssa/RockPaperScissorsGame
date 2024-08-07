import random
from Player import Player

class RandomPlayer(Player):
    def choice(self):
        choices = ['rock', 'paper', 'scissors']
        return random.choice(choices)