# package samples

#
# Program to convert Fahrenheit to Celsius
#
# This also shows the program structure we should try to adhere to
#
#         Input --> Process --> Output
#
#  To run: Right click in code > Run
#
def f2c_program():  # Program starts
    # ---- Input ----
    fahrenheit = float(input("Enter Fahrenheit > "))  # Print prompt to screen to notify user

    # ---- Process ----
    celsius = (fahrenheit - 32) * 5 / 9  # Some calculations (NO output here!)

    # --- Output ----
    print(f"{fahrenheit} F = {celsius} C")  # Output result to screen


if __name__ == "__main__":
    f2c_program()
