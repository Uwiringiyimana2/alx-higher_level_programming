#!/usr/bin/python3
"""
    This module adds two integers
"""

def add_integer(a, b=98):
    """ add two integers

    Args:
        a (int or float): integer
        b (int or float): integer

    Return:
        addition of a and b

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
