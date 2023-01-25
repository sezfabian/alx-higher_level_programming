#!/usr/bin/python3
"""Square module 2"""


class Square:
    """class Square
    Attributes
        _Square__size - size of square (integer)"""

    _Square__size = None

    def __init__(self, sizen=0):
        """Securely initializes class Square"""
        if sizen is not None:
            if isinstance(sizen, int) is False:
                raise TypeError("size must be an integer")
            elif sizen < 0:
                raise ValueError("size must be >= 0")
            else:
                self._Square__size = sizen
