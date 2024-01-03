#!/usr/bin/python3

'''
The module contains a function that prints a square with the character #
Module: 4-print_square.py
Function: print_square
'''


def print_square(size):
    '''Prints a square with the character #
    Parameter: size (integer)
    '''

    '''Validates float and > 0'''
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    '''Validates type'''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    '''Validates > 0'''
    if size < 0:
        raise ValueError("size must be >= 0")

    '''Prints the square with the character #'''
    for i in range(size):
        print("#" * size)
