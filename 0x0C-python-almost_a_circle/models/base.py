#!/usr/bin/python3
"""base class module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of an object (string)"""
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = str(cls.__name__) + ".json"
        dict1 = []
        if list_objs is not None:
            for i in list_objs:
                dict1.append(i.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dict1))
