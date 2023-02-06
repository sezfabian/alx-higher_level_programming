#!/usr/bin/python3
"""2-is_same_class module"""


def is_same_class(obj, a_clas):
    """returns True if the object is an instance of, \
    or if the object is an instance of a class that inherited from, \
    the specified class ; otherwise False"""
    isp = obj.__class__.__bases__
    if isinstance(obj, a_clas):
        return True
    else:
        return False
