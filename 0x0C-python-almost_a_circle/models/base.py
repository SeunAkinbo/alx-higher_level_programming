#!/usr/bin/python3
'''Module: base'''

import json
import csv
import turtle


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

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list of JSON string representation
        Args:
            - json_string
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns a class instance with all attributes already set
        Args:
            - dictionary
        '''
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances froma a JSON file'''
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding='utf-8') as file:
                json_str = file.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**obj_dict) for obj_dict in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Write the CSV string representation of list_objs to a file
        Args:
            - list_objs
        '''
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as file:
            writer = csv.writer(file)
            if list_objs:
                for obj in list_objs:
                    writer.writerow(obj.to_csv_row())
            else:
                writer.writerow([])

    @classmethod
    def load_from_file_csv(cls):
        '''Return a list of instance from a CSV file'''
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                return cls.format_csv_load(reader)
        except FileNotFoundError:
            return []

    def to_csv_row(self):
        '''Return the CSV representation of the instance'''
        raise NotImplementedError("to_csv_row method must be '\
                                    'implemented in the child class")

    @classmethod
    def format_csv_load(cls, csv_list):
        '''Return an instance from a CSV list'''
        raise NotImplementedError("create_from_csv_row method '\
                                    'must be implemented in the child class")

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.bgcolor("white")
        t = turtle.Turtle()
        t.speed(0)  # Set drawing speed to fastest

        def draw_shape(shape, color):
            t.penup()
            t.goto(shape.x, shape.y)
            t.pendown()
            t.color(color)

            for _ in range(4):
                t.forward(shape.width if isinstance(
                          shape, Rectangle) else shape.size)
                t.left(90)

        for rect in list_rectangles:
            draw_shape(rect, "black")

        for square in list_squares:
            draw_shape(square, "red")

        turtle.done()
