#!/usr/bin/python3

'''A 0-rectangle Module
'''


class Rectangle:
    '''A rectangle class
    '''
    def __init__(self, width=0, height=0):
        ''' __init__ initializing the class object with attribute
        Args:
            - width: A positive integer initialized to 0
            - heigth: A positive integer initialized to 0
        '''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Allows accessing the width attribute directly'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Allows modifying the width attribute directly
        Args:
            - value: A positive integer
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Allow accessing the heigth attribute directly'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Allow modifying the heigth attribute directly
        Args:
            - value: A positive integer
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
