#!/usr/bin/python3
""" class student module"""


class Student:

    def __init__(self, first_name, last_name, age):
        """ Initializes Student Class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary description with simple data structure \
                    (list, dictionary, string, integer and boolean) \
                    for JSON serialization of an object"""
        return self.__dict__
