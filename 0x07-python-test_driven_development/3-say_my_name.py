#!/usr/bin/python3
"""print my name module"""


def say_my_name(first_name, last_name=""):
    """prints a name, fisrt name then last name"""

    if not isinstance(first_name, str) or first_name == "":
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    elif last_name != "":
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
