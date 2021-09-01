# package samples

#
#  IO = Input/output, input data to program (here from keyboard) and
#  output data from program (to a terminal, a window)
# 
def io_program():
    print(1, end='')  # Print literal 1 to screen  (NO new line)
    print("abc")  # Print String literal and then new line
    print(" c d e ")  # Print String literal, spaces preserved
    print(f"My lucky number is {23}")  # Use formatted string to include expressions
    print("I can also " + "concatenate strings using + ")
    print()  # Just print new line
    print("Empty line above")

    # Must have some place to store input value(s), we use variable(s)
    n = int(input("Input an integer > "))  # Prompt user, read response

    # When running: Input some digits in bottom window (program will wait until Enter)
    print(f"Value was {n}")  # Text and content of variable written out!

    # NOTE: If NOT possible to convert input to the variable type, exception and program aborted (crash)
    # Run again: Try to input some non-digit characters and then enter

    s = input("Input some text > ")
    print("Value was " + s)  # We can concatenate strings using +


# Make file executable
if __name__ == "__main__":
    io_program()
