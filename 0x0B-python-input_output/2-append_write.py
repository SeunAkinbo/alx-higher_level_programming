#!/usr/bin/python3
'''Module: 2-append_write.py'''


def append_write(filename="", text=""):
    '''Afunction that appends string to the end of the file
    and returns the number of characters
    Args:
        - filename: The file path
        - text: String to write to file
    '''
    with open(filename, "a") as file:
        return file.write(text)
