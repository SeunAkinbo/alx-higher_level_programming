#!/usr/bin/python3

'''Module: 4-inherits_from'''


def inherits_from(obj, a_class):
    '''Checks for instance and inheritance'''
    return isinstance(obj, a_class) and type(obj) is not a_class
