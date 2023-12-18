#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except Exception as err:
            b += 1
            continue
    return result + b
