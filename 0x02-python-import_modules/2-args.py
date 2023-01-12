#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    print("{:d} arguments:".format(count))
    if count > 0:
        for i in range(1, count + 1):
            print('{:d}: {:s}'.format(i, argv[i]))
