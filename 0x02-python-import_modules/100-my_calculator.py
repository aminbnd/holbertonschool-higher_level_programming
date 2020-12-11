#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] == "+":
            res = add(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], res))
        elif argv[2] == "-":
            res = sub(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], res))
        elif argv[2] == "*":
            res = mul(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], res))
        elif argv[2] == "/":
            res = div(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], res))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
