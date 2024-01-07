#!/usr/bin/python3
""" This module divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """ divides all elements of a matrix

        Args:
            matrix: list of lists
            div (int or float): number

        Return:
            new matrix

        Raises:
            TypeError: matrix must be a list of lists of integers or floats
            ZeroDivisionError: div = 0
    """
    for row in matrix:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    result = []

    for row in matrix:
        for i in row:
            q = i / div
            result.append(round(q, 2))
        new_matrix.append(result)
    return new_matrix
