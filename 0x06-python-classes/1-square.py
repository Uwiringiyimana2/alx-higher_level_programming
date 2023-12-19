#!/usr/bin/python3
"""class Square defines square"""


class Square:
    """class square with private instance attributes: size"""

    def __init__(self, size):
        """Initialize the square instance

        Args:
            size (int): The size of the square
        """
        self.__size = size
