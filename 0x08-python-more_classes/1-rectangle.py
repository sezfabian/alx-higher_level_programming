#!/usr/bin/python3
""" Rectangle Class Module"""


class Rectangle:
    """ Rectangle Class"""
    def __init__(self, width=0, height=0):
        """Initializes Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Returns attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height value of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
