#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    operators = {'+' : add, '-' : sub, '*' : mul, '/' : div}

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = operators[operator](int(argv[1]), int(argv[3]))
    print(f"{argv[1]} {operator} {argv[3]} = {result}")
