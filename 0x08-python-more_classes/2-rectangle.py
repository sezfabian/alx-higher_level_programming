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
        """returns width of Rectangle"""
        return 2 * (self.height + self.width)
