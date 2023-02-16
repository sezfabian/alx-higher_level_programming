#!/usr/bin/python3
"""Rectangle class module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class Inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes Rectangle instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets Rectangle width value of rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """returns rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets Rectangle height value of rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """returns rectangle attr x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x attr of rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """returns rectangle attr y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y attr of rectangle"""
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns area of Rectangle"""
        return self.width * self.height

    def display(self):
        """prints rectangle instance with#"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute"""
        if len(args) > 5:
            raise TypeError("accepts less or 5 args")
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        else:
            if kwargs:
                for key, arg in kwargs.items():
                    if key == "id":
                        self.id = arg
                    if key == "width":
                        self.width = arg
                    if key == "height":
                        self.height = arg
                    if key == "x":
                        self.x = arg
                    if key == "y":
                        self.y = arg

    def to_dictionary(self):
        """ Returns a dictionary representation of the Rectangle Class """
        _dict = {'x': self.x, 'width': self.width, 'id': self.id,
                 'height': self.height, 'y': self.y}
        return _dict
