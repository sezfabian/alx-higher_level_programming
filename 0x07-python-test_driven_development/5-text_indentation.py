#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """Prints a text with 2 new lines \
    after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    Start = True
    for i in text:
        if Start and i == " ":
            continue
        if Start and i != " ":
            Start = False
        if Start is False:
            if i == "." or i == "?" or i == ":":
                print("{}\n".format(i))
                Start = True
            else:
                print(i, end="")
