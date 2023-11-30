#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv
    total = 0

    for i in range(len(args) - 1):
        total += int(args[i + 1])

    print(total)
