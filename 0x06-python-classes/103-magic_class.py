#!/usr/bin/python3

import math


class MagicClass:
    """
    Magic method
    """
    def __init__(self, radius=0):
        """This is a special method.

        Args:
            radius: the radius of the circle
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """Handles the area of the circle.

        Returns:
            float: The calculated area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Handles the circumference of the circle

        Returns:
            float: The calculated circumference of the circle.
        """
        return 2 * math.pi * self.__radius
