#!/usr/bin/python3
# baseed on 4-square.py by Kate Wuyep
"""A class that defines a square"""


class Square:
    """a class sqaure that defines a square"""

    def __init__(self, size=0):
        """initalizes the size
        Args: size which is defined as the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets value for the size
        Args: value
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Square instance can answer equal sign"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Square instance can answer not equal to sign"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Square instance can answer greater than sign"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Square instance can answer greater than oe equal to"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Square instance can answer less than sign"""
        return self.area() < other.area()

    def __le__(self, other):
        """Square instance can answer less than or equal to"""
        return self.area() <= other.area()
