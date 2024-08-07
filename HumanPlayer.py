from Player import Player


class HumanPlayer(Player):
    def choice(self):
        choices = ['rock', 'paper', 'scissors']
        choice = input("Please choice -> rock, paper, scissors:").lower()
        while choice not in choices:
            print("Invalid input!")
            choice = input("Please choice -> rock, paper, scissors:").lower()
        return choice
