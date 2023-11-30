#!/usr/bin/python3
def magic_calculation(a, b):

    # Initialize variables and functions
    add = None
    sub = None

    # Import add and sub functions from magic_calculation_102 module
    import magic_calculation_102
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
