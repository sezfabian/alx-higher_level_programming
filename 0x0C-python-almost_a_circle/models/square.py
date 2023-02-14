#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes Square Class instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {:d}/{:d} - {:d}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Returns the size of Square instance """
        return self.width

    @size.setter
    def size(self, size):
        """ Sets the size of square """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Assigns an argument key to each attribute"""
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            if kwargs:
                for key, arg in kwargs.items():
                    if key == "id":
                        self.id = arg
                    if key == "size":
                        self.size = arg
                    if key == "x":
                        self.x = arg
                    if key == "y":
                        self.y = arg

    def to_dictionary(self):
        """ Returns a dictionary representation of the Rectangle Class """
        _dict = {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
        return _dict
