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
        '''Validates the height and width attributes'''
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    def __validate_axis(self, attr_name, value):
        '''Validates the x and y arguments'''
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attr_name} must be >= 0")

    def to_dictionary(self):
        '''Return dictionary representation of the rectangle.'''
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

    def area(self):
        '''Returns the area of a rectangle'''
        return self.width * self.height

    def display(self):
        '''Prints the rectangle to the stdout'''
        if self.y != 0:
            print("\n" * (self.y - 1))
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
                f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        '''Updates the attributes using *args if available
        or kwargs attribute otherwise
        '''
        attrs = ["id", "width", "height", "x", "y"]

        if args:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    if attrs[i] == "id":
                        self.id = arg
                    if attrs[i] in ["width", "height"]:
                        self.__validate_side(attrs[i], arg)
                        setattr(self, attrs[i], arg)
                    if attrs[i] in ["x", "y"]:
                        self.__validate_axis(attrs[i], arg)
                        setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if key == "id":
                    setattr(self, key, value)
                if key in ["width", "height"]:
                    self.__validate_side(key, value)
                    setattr(self, key, value)
                if key in ["x", "y"]:
                    self.__validate_axis(key, value)
                    setattr(self, key, value)

    def to_csv_row(self):
        '''Return the CSV row representation of the Rectangle instance'''
        return [self.id, self.width, self.height, self.x, self.y]

    @classmethod
    def format_csv_load(cls, obj_list):
        '''Returns Rectangle instance from a CSV obj_list'''
        rect_list = []

        for row in obj_list:
            rect = cls(int(row[1]), int(row[2]), int(row[3]),
                       int(row[4]), int(row[0]))
            rect_list.append(rect)
        return rect_list
