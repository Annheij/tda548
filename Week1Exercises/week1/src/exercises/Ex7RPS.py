# package exercises

from random import random

# /*
#  * The Rock, paper, scissor game.
#  * See https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors
#  *
#  * This is exercising smallest step programming (no methods needed)
#  *
#  * Rules:
#  *
#  *       -----------  Beats -------------
#  *       |                              |
#  *       V                              |
#  *      Rock (1) --> Scissors (2) --> Paper (3)
#  *
#  */


def rps_program():
    max_rounds = 5
    human = 0               # Outcome for player
    computer = 0            # Outcome for computer
    result = 0              # Result for this round
    this_round = 0          # Number of rounds
    total: int = 0          # Final result after all rounds

    print("Welcome to Rock, Paper and Scissors")

    # TODO Write the game here. Use smallest step then surround with loop!!!!

    print("Game over!")
    if total == 0:
        print("Draw")
    elif total > 0:
        print("Human won.")
    else:
        print("Computer won.")


if __name__ == "__main__":
    rps_program()