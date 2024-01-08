#!/usr/bin/python3
'''Module: 5-base_geometry'''


class BaseGeometry:
    '''An empty class BaseGeometry'''

    def area(self):
        '''A method that computes the area of a geometry'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''A method that validates the value argument
        Args:
            - name: string argument
            - value: integer argument
        '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
