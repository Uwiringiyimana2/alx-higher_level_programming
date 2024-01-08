#!/usr/bin/python3
""" class Square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """square area"""
        return self.__size ** 2

    def __str__(self):
        """string repr"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
