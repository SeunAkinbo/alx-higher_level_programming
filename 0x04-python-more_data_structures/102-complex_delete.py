#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_del = []
    for key, val in a_dictionary.items():
        if val == value:
            key_del.append(key)
    for key in key_del:
        a_dictionary.pop(key)
    return a_dictionary
