#!/usr/bin/python3
""" module issubclass()."""


def inherits_from(obj, a_class):
    """
    Returns:
        True: if the object is exactly an instance of a class that inherited
        False: otherwise
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
