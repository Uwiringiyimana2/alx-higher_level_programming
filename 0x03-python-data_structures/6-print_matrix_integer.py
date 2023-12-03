#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """prints matrix"""
    if matrix:
        for row in matrix:
            for element in row:
                if element == row[0]:
                    print("{:d}".format(element), end="")
                else:
                    print(" {:d}".format(element), end="")
            print()
    else:
        print()
