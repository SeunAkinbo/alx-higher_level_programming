#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    argLen = len(argv) - 1
    operators = ['+', '-', '*', '/']

    if argLen == 3:
        if argv[2] not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        for operator in operators:
            if argv[2]  == operator and operator == operators[0]:
                print(f"{argv[1]} {argv[2]} {argv[3]} = {add(int(argv[1]), int(argv[3]))}")
                break
            elif argv[2] == operator and operator == operators[1]:
                print(f"{argv[1]} {argv[2]} {argv[3]} = {sub(int(argv[1]), int(argv[3]))}")
                break
            elif argv[2] == operator and operator == operators[2]:
                print(f"{argv[1]} {argv[2]} {argv[3]} = {mul(int(argv[1]), int(argv[3]))}")
                break
            elif argv[2] == operator and operator == operators[3]:
                print(f"{argv[1]} {argv[2]} {argv[3]} = {div(int(argv[1]), int(argv[3]))}")
                break
            else:
                continue
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
