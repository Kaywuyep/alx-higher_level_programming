#!/usr/bin/python3
"""an inhertance module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class of a square"""

    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.area()
