#!/usr/bin/python3
"""Square module 3"""


class Square:
    """class Square
    Attributes
        __size - size of square (integer)
    Methods
        Area - returns area of the square
        my_print - prints square in #"""

    def __init__(self, size=0, position=(0, 0)):
        """Securely initializes class Square"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        "initializes positions"
        if isinstance(value, tuple) is False or len(value) != 2 \
            or isinstance(value[0], int) is False or value[0] < 0\
            or isinstance(value[1], int) is False or \
                value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns area of square """
        return self.size * self.size

    def my_print(self):
        """prints in stdout the square with the character #"""
        for i in range(self.size):
            print(self.position[0] * "_" + self.size * "#")
        if self.size == 0:
            print()
