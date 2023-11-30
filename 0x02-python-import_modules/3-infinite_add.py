#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    args = argv
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
