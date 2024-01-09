#!/usr/bin/python3
'''Module: 0-read_file.py'''


def read_file(filename=""):
    '''The function reads a textfile
    Args:
        - filename: A text file path
    '''
    with open(filename, "r") as file:
        for char in file:
            print(char, end="")
