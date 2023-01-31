#!/usr/bin/python3
"""magic_string module"""


def magic_string():
    """returns a string “BestSchool” n times the number of the iteration """
    mystr = ""
    magic_string.counter += 1
    if magic_string.counter == 1:
        return "BestSchool"
    mystr = "BestSchool, " * (magic_string.counter - 1) + "BestSchool"
    return mystr


magic_string.counter = 0
