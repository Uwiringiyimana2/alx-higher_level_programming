#!/usr/bin/python3
"""defines class Rectangle."""


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes rectangle's width, height, x, y, id"""
        self.validate_rect(width, "width")
        self.__width = width
        self.validate_rect(height, "height")
        self.__height = height
        self.__x = x
        self.validate_xy(x, 'x')
        self.__y = y
        self.validate_xy(y, 'y')
        super().__init__(id)

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        self.validate_rect(value, "width")
        self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        self.validate_rect(value, "height")
        self.__height = value

    @property
    def x(self):
        """gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x"""
        self.validate_xy(value, 'x')
        self.__x = value

    @property
    def y(self):
        """gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y"""
        self.validate_xy(value, 'y')
        self.__y = value

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def validate_rect(self, value, attr_name):
        """validate width, height"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr_name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(attr_name))

    def validate_xy(self, value, attr_name):
        """validate x, y"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr_name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attr_name))

    def display(self):
        """prints in stdout the Rectangle"""
        for i in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """string representation of Rectangle"""
        str = f"{self.__width}/{self.__height}"
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " + str
