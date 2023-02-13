#!/usr/bin/python3
"""base class module"""


class Base:
    """Base Class defined"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes class instance"""
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects

    @property
    def id(self):
        """returns instance id"""
        return self.__id

    @id.setter
    def id(self, value):
        """sets instance id"""
        self.__id = value
