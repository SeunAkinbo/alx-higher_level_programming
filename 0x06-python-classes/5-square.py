#!/usr/bin/python3
# 5-square.py by Oluwaseun Akinbo

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
        """
        Property getter that allows accessing
        __size attribute indirectly
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter that allows modifying
        __size attribute indirectly
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes and return the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """Prints to the stdout the square with character #"""
        if self.size > 0:
            for i in range(self.size):
                print("#" * self.size)
        else:
            print()
