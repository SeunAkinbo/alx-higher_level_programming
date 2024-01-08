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

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        '''Returns the area of a rectangle'''
        return self.__width * self.__height
