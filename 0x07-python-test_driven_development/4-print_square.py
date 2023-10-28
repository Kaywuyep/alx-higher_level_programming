#!/usr/bin/python3
"""a module that prints a square"""


def print_square(size):
    """
    Prints a square

    :param size: size length of the square.
    :return: None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
