#!/usr/bin/python3
"""Square module 3"""


class Square:
    """class Square
    Attributes
        __size - size of square (integer)
    Methods
        Area - returns area of the square"""

    def __init__(self, sizen=0):
        """Securely initializes class Square"""
        self.size = sizen

    # getter
    @property
    def size(self):
        """Returns atribbute size"""
        return self.__size

    # setter
    @size.setter
    def size(self, value):
        """ sets size of square to value"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns area of square """
        return self.size * self.size
