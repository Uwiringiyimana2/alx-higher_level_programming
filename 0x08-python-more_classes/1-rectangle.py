#!/usr/bin/python3
""" defines class Rectangle"""


class Rectangle:
    """ empty rectangle """

    def __init__(self, width=0, height=0):
        """ Initializes rectangle

            Args:
                width: width of rectangle
                height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
