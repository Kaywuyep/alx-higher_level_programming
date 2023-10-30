#!/usr/bin/python3
"""a lazy-matrix module"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
    - m_a (list of lists): First matrix.
    - m_b (list of lists): Second matrix.

    Returns:
    - numpy.ndarray: Resulting matrix.

    Raises:
    - ValueError: If matrices can't be multiplied.
    """
    try:
        result = numpy.matmul(m_a, m_b)
        return result
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
