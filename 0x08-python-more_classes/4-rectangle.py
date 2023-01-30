#!/usr/bin/python3
"""Rectangle Class Module"""


class Rectangle:
    """defines class Rectangle"""

    def __init__(self, width=0, height=0):
        """initializes Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """returns Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets Rectangle width value of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets Rectangle height value of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """returns area of Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns perimeter of Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """returns class Rectangle as a string"""
        if self.height == 0 or self.width == 0:
            return ""

        rect = ""
        for i in range(self.height):
            rect += "#" * self.width
            if i < self.height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """returns accurate rep string of class instance"""
        if self.height == 0 and self.width == 0:
            return "Rectangle()"
        if self.width != 0 and self.height == 0:
            return "Rectangle({})".format(self.width)
        if self.height != 0:
            return "Rectangle({:d}, {:d})".format(self.width, self.height)
