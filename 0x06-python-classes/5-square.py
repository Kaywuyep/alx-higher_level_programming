#!/usr/bin/python3
# 4-square.py by Kate Wuyep
"""defines a square"""


class Square:
    """a class of square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        """
        self.size = size

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Args:
            value: represnets the size of the value defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculate and return the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()  # print empty line

        for i in range(self.__size):
            print("#" * self.__size)
