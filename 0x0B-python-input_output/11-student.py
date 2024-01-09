#!/usr/bin/python3
'''Module: 11-student.py'''


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

    def to_json(self, attrs=None):
        '''Returns the dictionary description of the student class
        Args:
            - attrs
        return: object dictionary
        '''
        obj_dict = {}
        if attrs is None:
            for key in self.__dict__:
                obj_dict[key] = getattr(self, key)
        else:
            for key in attrs:
                if hasattr(self, key):
                    obj_dict[key] = getattr(self, key)
        return obj_dict

    def reload_from_json(self, json):
        '''Replaces all attributes of the Student instance
        Args:
            - json: dictionary representing the attribute
        '''
        for key, value in json.items():
            setattr(self, key, value)
