#!/usr/bin/python3
'''Module: 9-student.py'''


class Student:
    '''class that defines a student'''
    def __init__(self, first_name, last_name, age):
        '''Initialize the class object
        Args:
            - first_name
            - last_name
            - age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Returns the dictionary description of the student class'''
        obj_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (str, int)):
                obj_dict[key] = value
        return obj_dict
