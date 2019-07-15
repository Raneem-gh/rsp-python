import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# 'sub classes: random, repeat, cycler, reflect, user'
class user(Player):

    def move(self):
        user_move = input("choose a move : (rock , scissors, paper)")
        user_move = user_move.lower()
        while user_move not in moves:
            print("Invalid input! try again")
            user_move = input("choose a move : (rock , scissors, paper)")
        return(user_move)

    def learn(self, my_move, their_move):
        pass


class Random(Player):

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class Repeat(Player):

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class Cycler(Player):
    index = 0

    def move(self):
        self.index += 1
        return moves[self.index % 3]

    def learn(self, my_move, their_move):
        pass


class Reflect(Player):
    index = 0

    def move(self):
        if self.index == 0:
            self.index += 1
            return random.choice(moves)
        else:
            return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("its a tie")
        elif beats(move1, move2):
            print("player 1 wins")
            self.p1.score += 1
        else:
            print("player 2 wins")
            self.p2.score += 1
        self.p2.learn(move1, move2)

    def play_game(self):
        print("Game start!")
        round = input("how many rounds will you play? ")
        for item in range(int(round)):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

        if self.p1.score > self.p2.score:
            print ("Player 1 Wins the game!")
        elif self.p2.score > self.p1.score:
            print ("Player 2 Wins the game!")
        else:
            print("the game ended with a TIE!")
# ask the player for another round
        while True:
            another_round = input("Play again?!!type again or quit:\t")
            if another_round == "quit":
                break
            elif another_round == "again":
                return game.play_game()
                break


if __name__ == '__main__':
    game_type = input("choose a game style: (random, cycler, repeat, reflect)")
    if game_type == "random":
        game = Game(user(), Random())
    # elif game_type = "cycler":
    #    game = Game(user(), Cycler())
    elif game_type == "repeat":
        game = Game(user(), Repeat())
    else:
        game = Game(user(), Reflect())
    game.play_game()
