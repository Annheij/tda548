# package samples

#  Types, literals and primitive variables
#
#  The primitive (built in) types (sets of values) in Python are
#  Numeric types:
#  - int, integers
#  - float, real numbers.
#  - complex, complex numbers.
#  - bool, truth values (are actually considered numeric)
#  Sequence types:
#  - list, mutable indexed containers.
#  - tuple, immutable indexed containers.
#  - range, immutable sequence of numbers
#  - str, immutable sequence of unicode characters
#  Sets and maps:
#  - set, unordered container of unique elements
#  - dict, mapping of unique keys to values
#
#  ... and a bunch of specialized ones that we don't need.
#
#  A literal is a fixed value in the code, like 6.7, 'S' or 396 (blue or green in PyCharm)
#  A literal never changes. A literal is automatically assigned a type
#  - 45 will be an int
#  - 3.6 will be a float. Note decimal separator is '.' (dot)
#  - True and False will be bool
#  - "Hello" or 'Hello' will be str (single or double quotes)
#
#  A variable in Python is an alterable container for a specific type of value.
#  It is highly recommended to not change the type of value held by a specific variable.
#
#  Variables in Python are not (cannot be!) declared before use.
#  - Initializing or assigning values to variables is done using the assignment operator '='
#
#  To change the value of a primitive variable we may use so called assignment operators,
#  such as += or *=.
def primitive_variables_program():
    # a               # Bad! Must initialize, like below (uncomment to see error message)
    a: int = 0  # Declare variable a, name and (optional) type, then initialize to 0
    b: int = 5  # 0 and 5 are integer literals (fixed values), automatically assigned type int
    # I.e. literals and variables are compatible (types matches)
    # a = 1.56         # Bad 1.56 is not an integer (uncomment to see error message)

    print(a)  # This will print 0 i.e. *value* in variable a on screen
    print(b)  # 5

    # ------ Assignment and in/decrement with ints ----------------
    a = 6  # 0 overwritten now a contains 6
    b = a  # 5 overwritten, replaced with a *copy* of a's value (a is still 6)
    print(b)  # 6

    # b++            # For those familiar with Java/C#/C++: No postfix increment/decrement in Python
    b += 1  # Increment value by one (short for b = b + 1)
    print(b)  # 7
    b -= 1  # Decrement
    print(b)  # 6

    a = a + 1  # + is addition. *Right side* of = evaluated first, then copied to left
    print(a)  # 7

    b = b + 2  # Again
    print(b)  # 9

    # -- Other primitive types/variables  -----------------------------
    bl: bool = True  # Note the capital letters for True/False
    print(f"{bl} has type {type(bl)}")
    f: float = 0.77  # 0.77 is a float literal, assigned type float
    print(f"{f} has type {type(f)}")

    s: str = "Hello world!"  # Single OR double quote for Strings. Anything in quotes is assign type str.
    print(f"{s} has type {type(s)}")
    s = ""  # The empty string, no character at all
    print(f"{s} has type {type(s)}")
