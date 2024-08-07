import random
from HumanPlayer import HumanPlayer
from RandomPlayer import RandomPlayer
from FixedPlayer import FixedPlayer
from RememberingPlayer import RememberingPlayer


class RockPaperScissorsGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0

# Paper > rock | rock > scissors | scissors > paper
    def result(self, choice1, choice2):
        if ((choice1 == 'paper' and choice2 == 'rock') or
                (choice1 == 'rock' and choice2 == 'scissors') or
                (choice1 == 'scissors' and choice2 == 'paper')):
            return True
        return False

    def round_result(self):
        choice1 = self.player1.choice()
        choice2 = self.player2.choice()

        if choice1 == choice2:
            print(f"It's a tie! Both players choice: {choice1}")
        elif self.result(choice1, choice2):
            print("Player 1 wins!")
            self.score1 += 1
        else:
            print("Player 2 wins!")
            self.score2 += 1

        print(f"Choice -> Player1: {choice1}, and Player2: {choice2}")
        print(f"Score -> Player1: {self.score1}, and Player2: {self.score2}")

        self.player1.lastGame(choice1, choice2)
        self.player2.lastGame(choice2, choice1)

    def start_game(self):
        print("Hello, Welcome To Rock Paper Scissors Game!")
        rounds = int(input("Enter number of rounds: "))
        for round in range(rounds):
            print(f"In Round {round+1}:")
            self.round_result()
        print("Final Result:")
        print(f"Score -> Player1: {self.score1}, and Player2: {self.score2}")
        if self.score1 > self.score2:
            print("Player 1 wins!")
        elif self.score1 < self.score2:
            print("Player 2 wins!")
        else:
            print("It's a tie!")
        print("Good Bye!")


if __name__ == '__main__':
    players = {
        '1': HumanPlayer,
        '2': RandomPlayer,
        '3': FixedPlayer,
        '4': RememberingPlayer
    }
    print("Player list:")
    for number, player in players.items():
        print(f"{number}. {player.__name__}")
    p1 = input("Choose player 1: ")
    while p1 not in players.keys():
        print("Invalid input! please select player 1")
        p1 = input("Choose player 1: ")
    p2 = input("Choose player 2: ")
    while p2 not in players.keys():
        print("Invalid input! please select player 2")
        p2 = input("Choose player 2: ")
    player1 = players[p1]()
    player2 = players[p2]()
    game = RockPaperScissorsGame(player1, player2)
    game.start_game()
