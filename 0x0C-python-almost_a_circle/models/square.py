#!/usr/bin/python3
'''Module: square'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''class Square that inherits from class Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initializing the Square class object'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''__str__ method update'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        '''Getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Updates the attributes using *args if available
        or kwargs attribute otherwise
        '''
        attrs = ["id", "width", "height", "x", "y"]

        if args:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Return the dictionary of the class attributes'''
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    def to_csv_row(self):
        '''Return the CSV row representation of the Square instance'''
        return [self.id, self.size, self.x, self.y]

    @classmethod
    def format_csv_load(cls, obj_list):
        '''Returns Square instance from a CSV obj_list'''
        sqr_list = []

        for row in obj_list:
            sqr = cls(int(row[1]), int(row[2]),
                        int(row[3]), int(row[0]))
            sqr_list.append(sqr)
        return sqr_list
