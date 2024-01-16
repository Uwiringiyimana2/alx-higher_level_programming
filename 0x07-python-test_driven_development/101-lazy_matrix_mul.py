#!/usr/bin/python3
"""multiplies 2 matrices by using the module NumPy"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices by using the module NumPy"""
    try:
        result = np.matmul(m_a, m_b)
        return result.tolist()
    except ValueError as e:
        raise ValueError("Error in matrix multiplication: {}".format(e))
