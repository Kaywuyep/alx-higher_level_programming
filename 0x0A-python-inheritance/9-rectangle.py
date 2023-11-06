#!/usr/bin/python3
"""an inheritance module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a rectangle class"""

    def __init__(self, width, height):
        """initialization"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """return string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
