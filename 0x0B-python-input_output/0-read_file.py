#!/usr/bin/python3
"""0-read_file module"""


def read_file(myfile):
    """prints contents of a file with UTF8 encoding"""

    with open(myfile, encoding="utf-8") as f:
        print(f.read())
