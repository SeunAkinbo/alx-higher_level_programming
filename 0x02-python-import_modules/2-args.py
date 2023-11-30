#!/usr/bin/python3
import sys

if __name__ == "__main__":

    args = sys.argv
    length = len(args)
    ac = length - 1

    if ac == 0:
        print("{} arguments.".format(ac))
    elif ac == 1:
        print("{} argument:".format(ac))
        print("{}: {}".format(ac, args[ac]))
    else:
        i = 1
        print("{} arguments:".format(ac))
        while i <= ac:
            print("{}: {}".format(i, args[i]))
            i += 1
