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
        super().validate_rect(value, "width")
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    def update(self, *args, **kwargs):
        """update class Square: assigns attributes."""
        attr_list = ["id", "size", 'x', 'y']
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for kw in kwargs.keys():
                if kw == "id":
                    self.id = kwargs[kw]
                if kw == "size":
                    self.size = kwargs[kw]
                if kw == 'x':
                    self.x = kwargs[kw]
                if kw == 'y':
                    self.y = kwargs[kw]

    def to_dictionary(self):
        """update class Square"""
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
