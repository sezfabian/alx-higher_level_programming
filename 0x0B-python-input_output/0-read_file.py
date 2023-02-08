#!/usr/bin/python3
"""0-read_file module"""


def read_file(myfile):
    """Reads contents of a file with UTF8 encoding and prints to stdout"""

    with open(myfile, encoding="utf-8") as f:
        print(f.read(), end="")
