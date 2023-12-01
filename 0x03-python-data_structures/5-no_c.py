#!/usr/bin/python3
def no_c(my_string):
    lst = []
    new_str = ""
    for char in my_string:
        lst.append(char)
    for char in lst:
        if char == 'c' or char == 'C':
            continue
        else:
            new_str += char
    return new_str
