#!/usr/bin/python3
def remove_char_at(str, n):
    strLen = len(str)
    words = ""
    index = 0
    for letter in str:
        if index != n:
            words += letter
        index += 1
    return (words)
