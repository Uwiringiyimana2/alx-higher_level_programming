#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        result = list(map(lambda x: x**2, i))
        new_matrix.append(result)
    return new_matrix
