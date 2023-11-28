#!/usr/bin/python3
for letter in "abcdefghijklmnopqrstuvwxyz"[::-1]:
    if ord(letter) % 2 == 1:
        letter = letter.upper()
    print("{}".format(letter), end='')
