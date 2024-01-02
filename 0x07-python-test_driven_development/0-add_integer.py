#!/usr/bin/python3
"""
The module computes two integers
Module: 0-add_integer
Function: add_integer
"""


def add_integer(a, b=98):
    """The function adds 2 integers
       Parameters: a and b=98
    """
    if not isinstance(a, (int, float)):
        """Checks if variable a is an integer or float"""
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        """Checks if variable b is an integer or float"""
        raise TypeError("b must be an integer")
    return int(a) + int(b)
