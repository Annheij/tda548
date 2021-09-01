# package exercises

# /*
#  *   Program to calculate the day number for same day in a given year.
#  *   - To check solution, see http://mistupid.com/calendar/dayofyear.htm
#  *
#  *   This is exercising functional decomposition
#  *   Assume you have a top level method solving the problem. Break down
#  *   top level method into smaller methods solving parts of the problem etc.
#  *   During this we run tests to make sure the methods works as expected.
#  *   Combine the method to solve the problem.
#  *
#  */
def day_number_program():
    # test();                // <--------- Uncomment to test only

    # -- In ----------------
    year = int(input("Input the year > "))
    month = int(input("Input the month number > "))
    day = int(input("Input the day number > "))

    # --- Process ---------
    # Write the code to call top level method here
    # Then break the method down in smaller methods, call them etc.
    day_nbr: int = 0    # TODO Replace 0 with a method that solves it!

    # ---- Out ----
    print_result(year, month, day, day_nbr)


def print_result(year: int, month: int, day: int, day_nbr: int):
    # TODO
    pass


# This is used to test methods in isolation
# Any non trivial method should be tested.
# If not ... can't build a solution out of possible failing parts!
def test():
    # TODO
    pass


if __name__ == "__main__":
    day_number_program()