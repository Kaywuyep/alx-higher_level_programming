#!/usr/bin/python3
"""
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """
    Divides all elements in the matrix by div.

    Args:
        matrix (list): A matrix (list of lists) of integers/floats.
        div (int or float): The number to divide all elements by.

    Returns:
        list: A new matrix with elements divided by div,
        rounded to 2 decimal places.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")

    size = None
    for row in matrix:
        # if type(row) is not list
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")

        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
