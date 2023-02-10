#!/usr/bin/python3
i = 122
flag = True
while i > 96:
    if flag is False:
        j = i - 32
    else:
        j = i
    flag = not flag
    print("{:c}".format(j), end="")
    i -= 1
