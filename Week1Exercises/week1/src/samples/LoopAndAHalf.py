# package samples

#  Loop and a half
#
#  This is used when the termination of the loop depends on
#  some value (input) in the loop
#
#
def loop_and_a_half_program():
    # Loop termination depends on user input
    while True:  # Infinite loop
        i = int(input("Input positive int > "))  # Try negatives when running!
        if i > 0:
            break  # Break in middle (half) of loop. Jump directly out of enclosing loop
    print("Loop ended")  # <--------- break jumps to here!
