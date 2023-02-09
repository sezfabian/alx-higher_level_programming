#!/usr/bin/python3
def uppercase(str):
    new = ""

    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            x = ord(str[i]) - 32
        else:
            x = ord(str[i])
        new = new + chr(x)
    print(new)
