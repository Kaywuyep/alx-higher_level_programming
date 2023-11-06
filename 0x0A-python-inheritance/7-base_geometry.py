#!/usr/bin/python3
"""a base geometry module"""


class BaseGeometry:
    """a base geometry class"""

    def area(self):
        """defined area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a function that validates the integer.
        assume 'name' is always a string"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            # since we assume name is always a string we can conceternate it
            raise ValueError(name + " must be greater than 0")
