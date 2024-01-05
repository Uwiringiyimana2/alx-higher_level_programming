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

    def area(self):
        """ returns rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ returns string representation of rectangle """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            result = ""
            for i in range(self.__height):
                result += '#' * self.__width + '\n'
            return result[:-1]

    def __repr__(self):
        """ returns string representation of the rectangle
        to be able to recreate a new instance """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ deletes rectangle """
        print("Bye rectangle...")