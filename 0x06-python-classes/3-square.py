#!/usr/bin/python3
# 0-square.py by Kate Wuyep
"""define a square"""


class Square:
    """class that defines a square"""
    def __init__(self, size=0):
        """ initializes the size
        Args:
            size: the size of the square
        Raises:
            TypeError and ValueError
        """
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """return current square area"""
        return (self.__size ** 2)  # or (self.__size * self.__size)
