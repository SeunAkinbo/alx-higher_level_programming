#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
    # return {k: v for k, v in a_dictionary.items() if k != key}
