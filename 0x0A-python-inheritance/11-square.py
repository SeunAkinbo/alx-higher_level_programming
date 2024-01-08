#!/usr/bin/python3
'''Module: 10-square.py'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A Square class that inherit from class Rectangle'''

    def __init__(self, size):
        '''Initialize the class object
        Args:
            - size (integer)
        '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''An area method returns the area of the square'''
        return self.__size ** 2

    def __str__(self):
        '''Returns the class Square string representation'''
        return f"[Square] {self.__size}/{self.__size}"
