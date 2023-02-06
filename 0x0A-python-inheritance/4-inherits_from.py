#!/usr/bin/python3
"""4-inherits_from.py module"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class \
    that inherited (directly or indirectly) from the specified class; \
    otherwise False"""

    isp = type(obj).__mro__
    if type(obj) != a_class:
        for i in isp:
            if i == a_class:
                return True
    return False
