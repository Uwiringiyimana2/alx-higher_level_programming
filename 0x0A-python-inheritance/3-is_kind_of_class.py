#!/usr/bin/python3
""" module isinstance()."""


def is_kind_of_class(obj, a_class):
    """
    Returns:
        True: if the object is exactly an instance of the specified class
        False: otherwise
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
