# package samples

from random import randint


# /**
#  * To select between different statements we use the if statement (selection)
#  *
#  * NOTE: We always put the statements in a block even if there is only one statement.
#  */
#    final Random rand = new Random();


def if_statement_program():
    i = randint(0, 9)  # Random int numbers
    j = randint(0, 9)
    k = randint(0, 9)

    # If statement
    if i == 2:  # if i equals 2 true ...
        print("i is 2")  # .. do this (note indentation)

    # If-else statement
    if j > 3:  # if j > 3 true ...
        print("j > 3")  # ... do this...
    else:  # ... else ... (note indentation)
        print("j <= 3")  # ... do this.

    # If-else if-statement (else if-ladder).
    # NOTE: Only one of alternatives is executed! If one true found
    # no other tested. If none found, else branch is executed.
    if j == 3:
        print("j is 3")
    elif k <= 20:
        print("k <= 20")
    else:
        print("j != 3 and k > 20")
