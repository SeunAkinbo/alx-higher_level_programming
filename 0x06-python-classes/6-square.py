#!/usr/bin/python3
"""A class Square File"""


class Square:
    """Defines a class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ Initializing the class object with attribute.
        Args:
        __size: A private instance attribute
        __position: A private instance attribute
        """
        self.__size = size
        self.__position = position

    def __str__(self):
        """prints the string"""
        self.my_print()

    @property
    def size(self):
        """Property getter that allows accessing
        __size attribute indirectly
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property getter that allows accessing
        __position attribute indirectly
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 values")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position elements must be non-negative integers")
        self.__position = value

    def area(self):
        """Computes and return the area of a square"""
        return self.size * self.size

    def my_print(self):
        """Prints to the stdout the square with character #,
        also, spaces for values at position[0] and newline
        where cordinates at  position[1] > 0
        """
        if self.size > 0:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
        else:
            print()
