#!/usr/bin/python3
"""Add two integers module"""


def add_integer(a, b=98):
    """adds two integers a and
    raises TypeError if a/b is not an integer"""
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    elif isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
