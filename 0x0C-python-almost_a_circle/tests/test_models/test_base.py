#!/usr/bin/python3
'''Module: test_base'''

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    def test_id_incremented(self):
        '''Test if the id is incremented correctly when not provided'''
        base_1 = Base()
        base_2 = Base()
        self.assertEqual(base_1.id, 3)
        self.assertEqual(base_2.id, 4)

    def test_id_assigned(self):
        '''Test if the id is assigned correctly when provided'''
        base_1 = Base(10)
        base_2 = Base(20)
        self.assertEqual(base_1.id, 10)
        self.assertEqual(base_2.id, 20)

    def test_id_incremented_after_assigned(self):
        '''Test if the id is incremented correctly after being assigned'''
        base_1 = Base(5)
        base_2 = Base()
        self.assertEqual(base_1.id, 5)
        self.assertEqual(base_2.id, 5)

    def test_id_type(self):
        '''Test if the id is an integer'''
        base = Base()
        self.assertIsInstance(base.id, int)

    def test_private_attribute(self):
        '''Test if the private attribute __nb_objects is not accessible'''
        base = Base()
        with self.assertRaises(AttributeError):
            base.__nb_objects

    def test_to_json_string(self):
        '''Testing the to_json_string method'''

        # Test with empty list
        empty_list = []
        result_empty = Base.to_json_string(empty_list)
        self.assertEqual(result_empty, "[]")

        # Test with a list of dictionaries
        dict_list = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        result_dict_list = Base.to_json_string(dict_list)
        expected_result = '[{"id": 1, "name": "Alice"},'\
            ' {"id": 2, "name": "Bob"}]'
        self.assertEqual(result_dict_list, expected_result)

        # Test with None
        result_none = Base.to_json_string(None)
        self.assertEqual(result_none, "[]")

    def test_save_to_file(self):
        '''Testing save_to_file'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            content = file.read()
        expected_output = '[{"id": 8, "width": 10, "height": 7, "x": 2, '\
            '"y": 8}, {"id": 9, "width": 2, "height": 4, "x": 0, "y": 0}]'
        self.assertEqual(content, expected_output)

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        with open("Square.json", "r", encoding="utf-8") as file:
            content = file.read()
        expected_output = '[{"id": 10, "size": 5, "x": 0, "y": 0}, {"id": 11, "size": 7, "x": 9, "y": 1}]'
        self.assertEqual(content, expected_output)

    def test_from_json_string(self):
        '''Testing from_json_string method'''
        
        # Test empty string
        result = Base.from_json_string("")
        self.assertEqual(result, '[]')

        # Test None
        result = Base.from_json_string(None)
        self.assertEqual(result, '[]')

        # Test valid JSON string
        json_string = '[{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]'
        result = Base.from_json_string(json_string)
        expected = [{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]
        self.assertEqual(result, expected)

    def test_create_method(self):
        '''Testing create method'''

        # Test creating a Rectangle instance with specific attributes
        rectangle_dict = {'id': 10, 'width': 5, 'height': 3}
        rectangle_instance = Rectangle.create(**rectangle_dict)
        self.assertIsInstance(rectangle_instance, Rectangle)
        self.assertEqual(rectangle_instance.id, 10)
        self.assertEqual(rectangle_instance.width, 5)
        self.assertEqual(rectangle_instance.height, 3)

        # Test creating a Square instance with specific attributes
        square_dict = {'id': 20, 'size': 4}
        square_instance = Square.create(**square_dict)
        self.assertIsInstance(square_instance, Square)
        self.assertEqual(square_instance.id, 20)
        self.assertEqual(square_instance.size, 4)

    def test_save_to_file_empty_list(self):
        '''Testing for an empty list'''
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            content = file.read()
        self.assertEqual(content, '[]')

        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as file:
            content = file.read()
        self.assertEqual(content, '[]')

    def tearDown(self):
        '''Deleting the files created during the test'''
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
