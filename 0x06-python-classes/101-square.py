#!/usr/bin/python3
"""A class Square File"""


class Square:
    """Defines a class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ Initializing the class object with attribute.

            Args:
            _size: A private instance attribute
        """
        self.__size = size
        self.__position = position

    def __str__(self):
        """
        Class instance
        """
        square_str = ""
        if self.__size == 0:
            return square_str + "\n"
        for _ in range(self.__position[1]):
            square_str += "\n"
        for i in range(self.__size):
            square_str += (" " * self.__position[0] + "#" * self.__size)
            if (i < self.__size - 1):
                square_str += "\n"
        return square_str

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Property getter that allows accessing
        __position attribute indirectly
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Property setter that allows modifying
        __position attribute indirectly
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes and return the area of a square"""
        return self.__size ** 2

    def my_print(self):
        '''Prints to the stdout the square with character #'''
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
        else:
            print()
