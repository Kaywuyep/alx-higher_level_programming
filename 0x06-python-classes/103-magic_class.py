#!/usr/bin/python3
"""Magic class module"""
import math
"""
In the Magic class we initialize each object by the
__init__ method with a private instance variable called
__radius that takes the radius variable's value passed as
argument.
"""


class MagicClass():
    """Magic class."""

    def __init__(self, radius=0):
        """Initialize radius"""
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return area of class."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return circumference of class."""
        return 2 * math.pi * self.__radius
