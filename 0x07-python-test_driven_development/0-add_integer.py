#!/usr/bin/python3
"""
The module computes two integers
>>> add_integer(12, 108)
120
"""


def add_integer(a, b=98):
    """The function adds 2 integers
       Args: a and b
    """
    if not isinstance(a, (int, float)):
        """Checks if variable a is an integer or float"""
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        """Checks if variable b is an integer or float"""
        raise TypeError("b must be an integer")
    return int(a) + int(b)
