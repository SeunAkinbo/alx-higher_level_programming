#!/usr/bin/python3
'''
A simple calculator function
'''
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    #create a dictionary of the operators
    operators = {'+' : add, '-' : sub, '*' : mul, '/' : div}
    #Checks for the number of arguments
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    #Checks for the operator
    operator = argv[2]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    #Performs the operation
    result = operators[operator](int(argv[1]), int(argv[3]))
    print(f"{argv[1]} {operator} {argv[3]} = {result}")
