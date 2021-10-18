import Calculator
from time import time


def test():

    input_char = '523+23+(3*2)^2'
    output = Calculator.tokenize(input_char)
    print(output == (['5', '2', '3', '+', '2', '3', '+', '(', '3', '*', '2', ')', '^', '2']))

    input_infix = ['5', '2', '3', '+', '2', '3', '+', '(', '3', '*', '2', ')', '^', '2']
    output = Calculator.infix_str_to_float(input_infix)
    print(output == ([523, '+', 23, '+', '(', 3, '*', 2, ')', '^', 2]))

    input_infix_float = [523, '+', 23, '+', '(', 3, '*', 2, ')', '^', 2]
    output = Calculator.infix_to_postfix(input_infix_float)
    print(output == [523, 23, '+', 3, 2, '*', 2, '^', '+'])

    postfix_float = [523, 23, '+', 3, 2, '*', 2, '^', '+']
    output = Calculator.eval_postfix(postfix_float)
    print(output == 582)

    input_char = '2^2^3'
    output = Calculator.eval_expr(input_char)
    print(output == 256)



if __name__ == "__main__":
    test()
