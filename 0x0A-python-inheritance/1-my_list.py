#!/usr/bin/python3
"""my_list class module"""


class MyList(list):
    """a class MyList that inherits from list"""

    def ___init__(self):
        """ Initiates MyList class """
        super().__init__()

    def print_sorted(self):
        """"prints MyList that is sorted in ascending"""
        print(sorted(self))
