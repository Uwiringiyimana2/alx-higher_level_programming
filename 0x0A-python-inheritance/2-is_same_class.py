#!/usr/bin/python3
""" module isinstance()."""


def is_same_class(obj, a_class):
    """
    Returns:
        True: if the object is exactly an instance of the specified class
        False: otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
