#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv
    length = len(args)
    total = 0
    index = 1

    if length == 1:
        print("{}".format(total))
    else:
        while index <  length:
            total += int(args[index])
            index += 1
        print("{}".format(total))
