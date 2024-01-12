#!/usr/bin/python3
'''Module: square'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''class Square that inherits from class Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initializing the Square class object'''
        super().__init__(size, size, x, y, id)
        if isinstance(size, int) and size > 0:
            self.size = size

    def __str__(self):
        '''__str__ method update'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
