#!/usr/bin/python3
# 4-square.py by Oluwaseun Akinbo

"""A class Square File"""


class Square:
    """Defines a class Square"""
    def __init__(self, size=0):
        """__init__ Initializing the class object with attribute.

            Args:
            _size: A private instance attribute
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
