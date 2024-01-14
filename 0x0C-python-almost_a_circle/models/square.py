#!/usr/bin/python3
"""class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square's size, x, y, and id."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets size."""
        return self.height

    @size.setter
    def size(self, value):
        """Sets size."""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
