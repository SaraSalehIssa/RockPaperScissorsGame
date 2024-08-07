import random
from Player import Player


class RememberingPlayer(Player):
    def __init__(self):
        self.last_choice = None

    def choice(self):
        if self.last_choice is None:
            return random.choice(['rock', 'paper', 'scissors'])
        return self.last_choice

    def lastGame(self, my_choice, their_choice):
        self.last_choice = their_choice
