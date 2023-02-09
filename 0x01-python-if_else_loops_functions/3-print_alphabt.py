#!/usr/bin/python3
for i in range(97, 122):
    if chr(i) != 'q' and chr(i) != 'e':
        print("{:c}".format(i), end="")
