#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """prints matrix"""
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print()
