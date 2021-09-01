# package exercises
#
#
#  Implement methods to make program produce correct output (normally print true)
#
# See:
# - MethodsBasics
# - MethodsArrObj  (just arrays)

def methods_program():
    # All should print true
    print(sum_to(5) == 15)     # 1 + 2 + ... + 5 = 15
    print(sum_to(23) == 276)
    print(factorial(3) == 6)    # 3 * 2 * 1 = 6
    print(factorial(5) == 120)
    print(digit_sum(1111) == 4)   # 1 + 1 + 1 + 1 = 4
    print(digit_sum(12345) == 15)

    arr = [10, 20, 30, 40, 50]
    print(next_in_list(arr, 2) == 40)    # Index 2 is 30 so next is 40.
    print(next_in_list(arr, 4) == 10)    # Index 4 is 50 so next is 10 (circular).


# ------ Write methods below this  -----------
def sum_to(n: int):
    # TODO
    return 0


# TODO More methods here
def factorial(n: int): pass
def digit_sum(n: int): pass
def next_in_list(in_list: list, index: int): pass


if __name__ == "__main__":
    methods_program()