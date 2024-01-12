#!/usr/bin/python3
'''Module: test_rectangle'''

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''class that test rectangle module'''
    def setUp(self):
        '''Assigning all parameters'''
        self.rect = Rectangle(10, 5, 2, 3, 1)

    def test_attributes(self):
        '''Test all attributes'''
        self.assertEqual(self.rect.id, 1)
        self.assertEqual(self.rect.width, 10)
        self.assertEqual(self.rect.height, 5)
        self.assertEqual(self.rect.x, 2)
        self.assertEqual(self.rect.y, 3)

    def test_setters(self):
        '''Test the setters'''
        self.rect.width = 15
        self.assertEqual(self.rect.width, 15)

        self.rect.height = 8
        self.assertEqual(self.rect.height, 8)

        self.rect.x = 5
        self.assertEqual(self.rect.x, 5)

        self.rect.y = 7
        self.assertEqual(self.rect.y, 7)

    def test_invalid_width(self):
        '''Testing for invalid width'''
        with self.assertRaises(ValueError):
            self.rect.width = -5

    def test_invalid_height(self):
        '''Testing for invalid height'''
        with self.assertRaises(ValueError):
            self.rect.height = -3

    def test_invalid_x(self):
        '''Testing for invalid x'''
        with self.assertRaises(ValueError):
            self.rect.x = -2

    def test_invalid_y(self):
        '''Testing for invalid y'''
        with self.assertRaises(ValueError):
            self.rect.y = -1

    def test_invalid_type_width(self):
        '''Testing for invalid type width'''
        with self.assertRaises(TypeError):
            self.rect.width = "9"

    def test_invalid_type_height(self):
        '''Testing for invalid type height'''
        with self.assertRaises(TypeError):
            self.rect.height = "9"

    def test_invalid_type_x(self):
        '''Testing for invalid type x'''
        with self.assertRaises(TypeError):
            self.rect.x = "9"

    def test_invalid_type_y(self):
        '''Testing for invalid type y'''
        with self.assertRaises(TypeError):
            self.rect.y = "9"

    def test_area(self):
        '''Testing for area'''
        rect_1 = Rectangle(5, 10)
        self.assertEqual(rect_1.area(), 50)

        with self.assertRaises(ValueError):
            rect_2 = Rectangle(0, 8)
            rect_2.area()
        
        with self.assertRaises(ValueError):
            rect_3 = Rectangle(-2, 7)
            rect_3.area()


if __name__ == '__main__':
    unittest.main()
