#!/usr/bin/python3
'''Module: 1-write_file.py'''


def write_file(filename="", text=""):
    '''
    Writes a string text to the file and returns the number of characters
    written

    Args:
        - filename: File path
        - text: to be written to file
    '''
    with open(filename, "w") as file:
        return file.write(text)
