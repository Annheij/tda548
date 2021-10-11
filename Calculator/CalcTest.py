import Calculator

def test():
    input = '523+23+3'
    output = Calculator.tokenize(input)
    print(output == [['5'+'5'+'2'], '+', '23', '+', '3'])

    output = Calculator.infix_to_postfix(input)
    print(output == ['1', '2', '+', '3', '+'])


if __name__ == "__main__":
    test()
