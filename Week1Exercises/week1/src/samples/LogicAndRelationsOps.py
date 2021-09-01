# package samples

# /**
#  * Logical and relational operators
#  */
def logic_and_relations_program():
    # Logical operators (don't care about warnings) ---

    print(not False)  # Negation
    print(not not True)
    print(True & True)  # Logical and
    print(True | False)  # Logical or

    # Equality and relational operators (don't care about warnings) ---

    print(1 == 1)  # Equal. NOTE two "=" !!!
    print(1 != 2)  # Not equal
    print(2 > 1)  # Bigger than etc.
    print(1 < 2)
    print(1 <= 1)
    print(1 >= 1)

    # Compound use of (don't care about warnings) ----------

    i: int = 4
    print(1 <= i & i <= 8)  # i in closed interval [1,8]
    print(i < 1 | 8 < i)  # i is *not* in closed interval [1,8]

    b: bool = True
    print((i >= 4) & b)  # i greater or equal to 4 and b is True?

    s = input("Input string: abc > ")
    print(s == "abc")   # Equality on strings
    print(s > "abc")    # Comparison operators on strings
    print(s.isalpha())
    print(s.islower())
    # TODO explore what other tests you can do on strings


if __name__ == "__main__":
    logic_and_relations_program()
