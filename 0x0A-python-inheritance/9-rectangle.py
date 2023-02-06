#!/usr/bin/python3
"""9-rectangle module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """ Rectangle Sub Class of BaseGeometry """

    def __init__(self, width, height):
        """initializes subclass rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        if not self.__width or not self.__height:
            return
        return self.__width * self.__height

    def __str__(self):
        """returns rectangle description"""
        rect = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return rect
