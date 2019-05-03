#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argc = len(sys.argv) - 1
    argv = sys.argv
    operators = {'+':'add(a, b)', '-':'sub(a, b)', '*':'mul(a, b)', '/':'div(a, b)'}

    if argc is not 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>:")
        exit(1)
    elif not argv[2] in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        print("{} {} {} = {}".format(a, argv[2], b, eval(operators[argv[2]])))
