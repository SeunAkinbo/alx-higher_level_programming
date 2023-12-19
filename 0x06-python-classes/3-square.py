#!/usr/bin/python3
# 3-square.py by Oluwaseun Akinbo

"""A class Square File"""


class Square:
    """Defines a class Square"""
    def __init__(self, size=0):
        """__init__ Initializing the class object with attribute.

            Args:
            _size: A private instance attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
