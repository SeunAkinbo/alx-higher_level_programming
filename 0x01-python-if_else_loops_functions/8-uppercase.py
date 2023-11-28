#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        asc = ord(letter)
        if asc > 96 and asc < 123:
            asc -= 32
        print("{}".format(chr(asc)), end='')
