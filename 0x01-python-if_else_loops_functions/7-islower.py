#!/usr/bin/python3
def islower(c):
    asc = ord(c)
    if asc < 98 and asc < 123:
        return (True)
    else:
        return (False)
