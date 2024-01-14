#!/usr/bin/python3
"""This module defines class Base."""


class Base:
    """base of all other classes of this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initiliazes id"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
