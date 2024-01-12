#!/usr/bin/python3
'''Module: rectangle'''

from models.base import Base


class Rectangle(Base):
    '''class Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize the class object'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Getter for width attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width attribute
        Args:
            - value: integer
        '''
        self.__validate_side("width", value)
        self.__width = value

    @property
    def height(self):
        '''Getter for height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height attribute
        Args:
            - value: integer
        '''
        self.__validate_side("height", value)
        self.__height = value

    @property
    def x(self):
        '''Getter for the x-axis attribute'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x-axis attribute
        Args:
            - value: integer
        '''
        self.__validate_axis("x", value)
        self.__x = value

    @property
    def y(self):
        '''Getter for y-axis attribute'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y-axis attribute
        Args:
            - value: integer
        '''
        self.__validate_axis("y", value)
        self.__y = value

    def __validate_side(self, attr_name, value):
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    def __validate_axis(self, attr_name, value):
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attr_name} must be >= 0")

    def area(self):
        '''Returns the area of a rectangle'''
        return self.width * self.height

    def display(self):
        '''Prints the rectangle to the stdout'''
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
                f"{self.width}/{self.height}"