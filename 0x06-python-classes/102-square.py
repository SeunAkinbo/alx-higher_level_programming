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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        """Compare equality"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare not equal to"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare greater than or equal to"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compare less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare less than or equal to"""
        return self.area() <= other.area()
