from Player import Player

class HumanPlayer(Player):
    def choice(self):
        choices = ['rock', 'paper', 'scissors']
        choice = input("Please enter one choice -> rock, paper, scissors:").lower()
        while choice not in choices:
            choice = input("Invalid input! Enter rock, paper, or scissors:").lower()
        return choice