#!/usr/bin/python3
"""
Contains the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices(lists of lists of integers/floats)
    Args:
    - m_a (list of lists): First matrix.
    - m_b (list of lists): Second matrix.

    Returns:
    - list of lists: Resulting matrix.

    Raises:
    - TypeError: If m_a or m_b is not a list, not a list of lists,
                 or contains non-integer/float elements.
    - ValueError: If m_a or m_b is empty, or if matrices can't be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    l1 = len(m_a)
    if l1 == 0:
        raise ValueError("m_a can't be empty")
    l2 = None
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if l2 is None:
            l2 = len(row)
            if l2 == 0:
                raise ValueError("m_a can't be empty")
        if l2 != len(row):
            raise TypeError("each row of m_a must should be of the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    l3 = None
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if l3 is None:
            l3 = len(row)
            if l3 == 0:
                raise ValueError("m_b can't be empty")
        if l3 != len(row):
            raise TypeError("each row of m_b must should be of the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    if l2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(l1):
        l = []
        for j in range(l3):
            n = 0
            for k in range(l2):
                n += m_a[i][k] * m_b[k][j]
            l.append(n)
        matrix.append(l)
    return matrix
