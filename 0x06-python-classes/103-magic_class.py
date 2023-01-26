#!/usr/bin/python3
""" Magiclass module
"""
import math


class MagicClass:
    """ Magiclass
    """

    def __init__(self, radius=0):
        """ Class instance initialization

        Args:
            radius (int, optional): radius for the magic class. Defaults to 0.

        Raises:
            TypeError: radius must be a number
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
