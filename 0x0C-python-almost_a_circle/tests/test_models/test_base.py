#!/usr/bin/python3
'''Module: test_base'''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_incremented(self):
        '''Test if the id is incremented correctly when not provided'''
        base_1 = Base()
        base_2 = Base()
        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 2)

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
        self.assertEqual(base_2.id, 3)

    def test_id_type(self):
        '''Test if the id is an integer'''
        base = Base()
        self.assertIsInstance(base.id, int)

    def test_private_attribute(self):
        '''Test if the private attribute __nb_objects is not accessible'''
        base = Base()
        with self.assertRaises(AttributeError):
            base.__nb_objects


if __name__ == '__main__':
    unittest.main()
