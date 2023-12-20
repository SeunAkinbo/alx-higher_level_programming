#!/usr/bin/python3
"""Magic method"""
import math


class MagicClass:
    """set up the magic"""

    def __init__(self, radius=0):
        """ writing docstring """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Area of a circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Circumfrence of a circle"""
        return 2 * math.pi * self.__radius
