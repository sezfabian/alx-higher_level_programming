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
