import Calculator
from time import time
def test():
    time_start = time()
    input_char = '523+23+(3*2)^2'
    output = Calculator.tokenize(input_char)
    print(output == (['5', '2', '3', '+', '2', '3', '+', '(', '3', '*', '2', ')', '^', '2']))
    time_end = time()
    print(time()-time_start)

    time_start = time()
    input_infix = ['5', '2', '3', '+', '2', '3', '+', '(', '3', '*', '2', ')', '^', '2']
    output = Calculator.infix_str_to_float(input_infix)
    print(output == ([523, '+', 23, '+', '(', 3, '*', 2, ')', '^', 2]))
    print(time()-time_start)

    time_start = time()
    input_infix_float = [523, '+', 23, '+', '(', 3, '*', 2, ')', '^', 2]
    output = Calculator.infix_to_postfix(input_infix_float)
    print(output == [523, 23, '+', 3, 2, '*', 2, '^', '+'])
    print(time()-time_start)

    time_start = time()
    postfix_float = [523, 23, '+', 3, 2, '*', 2, '^', '+']
    output = Calculator.eval_postfix(postfix_float)
    print(output == 582)
    print(time()-time_start)

        #Bongiorno you sweet sexy man
if __name__ == "__main__":
    test()
