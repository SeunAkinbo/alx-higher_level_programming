#!/usr/bin/python3
"""Unit tests for Square class."""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_init(self):
        """Test initialization of Square instance."""
        s1 = Square(5, 1, 2, 10)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 10)

    def test_size_property(self):
        """Test size property."""
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
