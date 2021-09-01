# package exercises

# from random import *


# /*
#  *  The TicTacToe Game
#  *  See https://en.wikipedia.org/wiki/Tic-tac-toe.
#  *
#  *  This is exercising functional decomposition and testing
#  *  - Any non trivial method should be tested (in test() method far below)
#  *  - IO methods never tested.
#  *
#  *  NOTE: Just use an array for the board (we print it to look square, see plotBoard())
#  *
#  */
def tic_tac_toe_program():
    # test()       # <--------- Comment out to test

    p1: Player = Player("olle", 'X')
    p2: Player = Player("fia", 'O')
    current = None  # For now
    winner = None
    board = create_board()

    print("Welcome to Tic Tac Toe, board is ...")
    plot_board(board)

    # TODO Add game logic here (use smallest step and functional decomposition)

    print("Game over!")
    plot_board(board)

    if winner is not None:
        print("Winner is " + current.name)
    else:
        print("Draw")


# ---------- Methods below this ----------------
# TODO More methods


def create_board():
    board = []
    for i in range(9):
        board[i] = " "
    return board


def get_player_selection(player):
    while True:
        print("Player is " + player.name + "(" + player.mark + ")")
        selection = int(input("Select position to put mark (0-8) > "))
        if 0 <= selection & selection <= 8:
            break
        print("Bad choice (0-8 allowed)")
    return selection


def plot_board(board):
    for i in range(len(board)):
        print(board[i] + " ")
        if (i + 1) % 3 == 0:
            print("\n")


# A class (blueprint) for players.
class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


# This is used to test methods in isolation
# Any non trivial method should be tested.
# If not ... can't build a solution out of possible failing parts!
def test():
    b = create_board()
    print(len(b) == 9)
    # TODO More tests


if __name__ == "__main__":
    tic_tac_toe_program()