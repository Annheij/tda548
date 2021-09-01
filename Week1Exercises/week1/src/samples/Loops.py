# package samples

# /*
#  * To repeat a number of statements we use loops i.e. the while and for
#  * loops (iteration)
#  *
#  * NOTE: We always put the statements in a block even if there is only one statement to repeat.
#  */
def loops_program():
    # ----- while loop  ------------
    # Used when we don't know the number of iterations

    # Going up
    i = 0  # Set start value for counter
    while i < 5:
        print("i is : " + str(i))  # ... yes, do the block (else continue after block)
        i += 1  # Increment counter (always last)
        # Jump up to while and start over
    print("i after loop is : " + str(i))

    # Going down
    i = 5
    while i > 0:
        print("i is : " + str(i))
        i -= 1  # Decrement counter
    print("i after loop is : " + str(i))

    # Step
    i = 0
    while i < 10:
        print("i is : " + str(i))
        i = i + 2  # Step by 2
    print("i after loop is : " + str(i))

    # Non terminating (program will hang, program running but nothing seems to happen)
    # Uncomment and run to try
    #
    # value = 0
    # while (value >= 0) {    # True forever
    #    print("i is : " + str(value))
    #    value += 1

    # --- for loop  -------------------
    # Used when we DO know the number of iterations

    # Going up
    for j in range(5):  # If j < 5 is true ...
        print("j is : " + str(j))  # ... execute the block (else continue after loop)
        # <------ j++ is in fact done here (lastly), but written on first line
        # Jump up to j < 5, and start over

    # Can use j here, despite warning, scoping in Python is weird! Or dynamic, rather...
    print("After, j is " + str(j))

    # Going down
    for j in reversed(range(10)):
        print("j is : " + str(j))

    # Step by 2
    for k in range(0, 20, 2):
        print("k is : " + str(k))


if __name__ == "__main__":
    loops_program()
