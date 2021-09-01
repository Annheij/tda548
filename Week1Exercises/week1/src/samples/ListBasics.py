# package samples

#
# To package variables of the same type we use a List. A list is an object containing a
# consecutive "row" of variables (elements) that are (typically, preferably) of the same type.
# To access individual variables we use indices (the order number for the variable).
# Indexing starts at 0! So last element index is (length - 1)
# If using index outside, an exception will be thrown (program crash, more later in the course)
#
# The length of the list (the number of variables) is specified during the initialization
# of a list variable. If we want to increase the length of the list, we can use the "append" method.
# Later we can read the length of the list object by using len(list), see examples below
#
#
def list_basics_program():
    # Declare list variable and initialize it
    # Will create 5 int variables (with the common name "my_list") and set values at index 0 to 4.
    my_list = [7, 1, 0, 4, -2]

    print(my_list)

    print(my_list[0])  # Use index to read and print value of single variable in the list
    print(my_list[3])  # First element is at index 0, so index 3 gives 4th variable

    # --- Some manipulation, using indices ------------
    my_list[0] = 2  # Assign using index
    my_list[2] = my_list[3]
    n = 8
    my_list[1] = n
    n = my_list[2]
    print(n)
    # my_list[4]++       # No postfix increment operator!
    my_list[4] += 1      # Increment using assignment operator
    print(my_list)

    # my_list[5] = 0      # IndexError, index outside length of list

    j = 2  # Variables for indexing
    my_list[j] = 99
    my_list[j + 1] = my_list[j]  # Indexing may use expressions
    print(my_list)

    # --- Create lists in different ways
    my_list = [0] * 6  # Variable my_list already declared. Reuse it!
    # Create new list with 6 variables with value 0.
    # Note that * operator is overloaded for lists to mean repetition
    print(my_list)

    # -------------------------------------------
    my_list2 = [6, 7, 8]  # This is another declaration and initialization, a new variable my_list2

    # ------- Traversing -----------------
    # To visit all variables in turn (left to right or the reverse) is called traversing.

    # Default way to get length of a list
    print(f"Length of list is {len(my_list2)}")

    # Going left to right. Use for loop + length to traverse with index.
    for i in range(len(my_list2)):
        print(f"{2 * my_list2[i]} ")  # Just some dummy output
    print("\n")  # A new (empty) line, just formatting

    # Same left to right in an easier way, if index values are not needed.
    for item in my_list2:
        print(f"{2 * item} ")

    # Going right to left
    for i in range(len(my_list2)):
        print(f"{3 * my_list2[-i - 1]} ")  # Just some dummy output
    print("\n")  # A new (empty) line, just formatting

    # ----  Lists and IO  --------------------------
    names = []  # Declare and create a list of length 0

    nr_names = int(input("How many names do you want to input? "))
    print(f"Input {nr_names} names (enter after each) > ")  # Read strings into list
    for _i in range(nr_names):  # Must use loop
        names.append(input())  # Read an element, we use append to extend the list step by step

    print(f"Length is now {len(names)}")
    print("Names are:")  # Write content of array to screen
    for name in names:
        print(name)


# Make program executable
if __name__ == "__main__":
    list_basics_program()
