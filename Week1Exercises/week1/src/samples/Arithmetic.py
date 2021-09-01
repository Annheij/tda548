# package samples

#
#  Arithmetic with Java, mostly as you are used to in math.
#
def arithmetic_program():
    op1 = int(input("Input 2 integers (enter after each) > "))  # Prompt user
    op2 = int(input())

    # All below are statements
    # The right side is an expression, i.e a value. Right side calculated first!
    # Always a variable to the left.
    result = op1 + op2                # Addition.
    print(f"Result + {result}")

    result = op1 - op2                # Subtraction
    print(f"Result - {result}")

    result = op1 * op2                # Multiplication
    print(f"Result * {result}")

    result = op1 // op2               # Division. Oh, oh, ..
    print(f"Result / {result}")       # ... this is integer division!

    result = op1 / op2                # Now we get real division
    print(f"Result real / {result}")

    result = op1 % op2                       # Remainder operator (modulo)
    print(f"Result % (modulo) {result}")

    print(f"Left to right {4/2/2}")          # Associativity (Left to right normally)
    print(f"Using parentheses {4/(2/2)}")

    result = 4 + 6 / 3 * 2                   # Whats is above/below the division sign?
    print(f"Result priority 1 {result}")

    result = 4 + 6 / (3 * 2)                 # Use parentheses to get correct result!
    print(f"Result priority 2 {result}")

    result = -op1                            # Negation
    print(f"Result unary - {result}")

    result = op1 ** op2                      # exp/power operator like ^
    print(f"Result ** {result}")

    # print(f"Div with zero {1/0}")          # ZeroDivisionError


if __name__ == "__main__":
    arithmetic_program()
