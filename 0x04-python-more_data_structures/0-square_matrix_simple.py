#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    # for i = row and j = column
    new_mat = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_mat[i][j] = matrix[i][j] ** 2

    return new_mat
