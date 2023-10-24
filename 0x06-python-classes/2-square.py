#!/usr/bin/python3
# 0-square.py by Kate Wuyep
"""A module that defines a square """


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """defines a square
        Args:
            size: represent size of square
        Raises:
            TypeError and ValueError
        """
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
