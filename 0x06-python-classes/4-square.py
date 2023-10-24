#!/usr/bin/python3
# 3-square.py by Kate Wuyep
"""defines a square"""


class Square:
    """a class square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.size = size

    @property
    def size(self):
        """retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Raises:
        TypeError and ValueError
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """
        return self.__size * self.__size
