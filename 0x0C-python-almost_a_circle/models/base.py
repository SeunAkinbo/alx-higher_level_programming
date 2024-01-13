#!/usr/bin/python3
'''Module: base'''

import json


class Base:
    '''Base Class
    - __nb_objects: Private class attribute
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialize the class object'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Static method that returns a json string
        of the dictionary attributes
        Args:
            - list_dictionaries: Dictionary of class attributes
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves the JSON string representation to a file
        Args:
            - list_objs: Dictionary of class attributes
        '''
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            # Writing to a JSON file
            json_str = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])
            file.write(json_str)
