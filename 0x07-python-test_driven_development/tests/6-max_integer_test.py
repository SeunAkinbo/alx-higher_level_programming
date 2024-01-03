#!/usr/bin/python3
'''Unit test for max_integer
'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Class test for max_integer
    inherits - unittest.TestCase
    '''
    def test_max_integer(self):
        '''Function test for max integer'''
        param = [1, 5, 9, 12, 11, 56]
        result = max_integer(param)
        self.assertEqual(result, 56)
