#!/usr/bin/python3
"""square module1"""


class Square:
    """class Square"""

    _Square__size = None

    def __init__(self, sizen=None):
        """initializes the class Square"""
        if sizen is not None:
            self._Square__size = sizen
