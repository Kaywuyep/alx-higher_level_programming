#!/usr/bin/python3
"""an inhertance module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialization
        Note: width and height are assigned the value 'size'
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """attribute getter, to retrieve size"""
        return self.width

    @size.setter
    def size(self, value):
        """attribute setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """return the string format"""
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__,
                self.id,
                self.x,
                self.y,
                self.width
                )

    def update(self, *args, **kwargs):
        """
        args:
            *args - non keyworded arguments
            **kwargs - key worded arguments
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation
        """
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
