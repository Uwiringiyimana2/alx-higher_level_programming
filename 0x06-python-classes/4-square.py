#!/usr/bin/python3
"""class Square defines square"""


class Square:
    """class square with private instance attributes: size"""

    def __init__(self, size=0):
        """Initialize the square instance

        Args:
            size (int, optional): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.__size = size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter

        Args:
            value(int): the size to set

         Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """public instance method of class square

        Return:
            int: the current square area
        """
        return self.__size ** 2
