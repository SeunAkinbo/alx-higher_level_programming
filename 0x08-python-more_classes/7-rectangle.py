#!/usr/bin/python3

'''A 0-rectangle Module
'''


class Rectangle:
    '''A rectangle class
    class attribute - number_of_instances
    '''
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''Function computes the area of a rectangle'''
        return self.height * self.width

    def perimeter(self):
        '''Function computes the perimeter of a rectangle'''
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

    def __str__(self):
        '''Returns the rectangle using # character '''
        rect = ""
        if self.height == 0 or self.width == 0:
            return rect
        else:
            for _ in range(self.height):
                rect += str(self.print_symbol) * self.width
                if _ != self.height - 1:
                    rect += "\n"
            return rect

    def __repr__(self):
        '''Returns the rectangle dimension'''
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        '''Prints the delete rectangle message'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
