#!/usr/bin/python3

'''Module: 8-rectangle'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle that inherits from BaseGeometry'''

    def __init__(self, width, height):
        '''Initializing class Rectangle
        Args:
            - width (integer)
            - height (integer)
        '''
        Rectangle.integer_validator(self, "width", width)
        self.__width = width
        Rectangle.integer_validator(self, "height", height)
        self.__height = height
