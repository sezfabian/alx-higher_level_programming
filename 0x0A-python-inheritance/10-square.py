#!/usr/bin/python3
"""10-square module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle (9-rectangle.py)"""

    def __init__(self, size):
        """initializes object square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
