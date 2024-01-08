#!/usr/bin/python3
"""Module of class BaseGeometry"""


class BaseGeometry:
    """ base_geometry """

    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value."""
        if not isinstance(name, str):
            raise TypeError
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
