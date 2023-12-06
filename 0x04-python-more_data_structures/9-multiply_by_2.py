#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    '''
    new = {}
    for key, value in a_dictionary.items():
        new[key] = value * 2
    return new
    '''
    return {key: value * 2 for key, value in a_dictionary.items()}
