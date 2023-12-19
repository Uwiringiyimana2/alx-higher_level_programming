#!/usr/bin/python3
"""class Square defines square"""


class Square:
    """class square with private instance attributes: size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square instance

        Args:
            size (int, optional): The size of the square
            position (tuple, optional): position of square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """Getter to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """validate a position attribbute

        Args:
            value: position to set

        Raises:
            TypeError: if not 2 positive number
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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

    def my_print(self):
        """prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        returns string version of square
        """
        string = ""
        if self.__size == 0:
            return string
        string += '\n' * self.__position[1]
        for i in range(self.__size):
            string += " " * self.__position[0]
            string += "#" * self.__size
            if i < self.__size - 1:
                string += "\n"
        return string
