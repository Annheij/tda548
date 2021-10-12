import Calculator

def test():
    input = '523+23*3'
    output = Calculator.tokenize(input)
    print(output == (['5', '2', '3', '+', '2', '3', '*', '3']))

    input = output
    output = Calculator.give_reference(input)
    print(output == ([523, '+', 23, '*', 3]))

    input = output
    output = Calculator.infix_to_postfix(input)
    print(output == [523, 23, 3, '*', '+'])

    input = output
    output = Calculator.eval_postfix(input)
    print(output == [])


if __name__ == "__main__":
    test()
