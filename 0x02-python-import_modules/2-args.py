#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print ("1 argument:")
    else:
        print("{:d} arguments:".format(count))
    if count > 0:
        for i in range(1, count + 1):
            print('{:d}: {:s}'.format(i, argv[i]))
