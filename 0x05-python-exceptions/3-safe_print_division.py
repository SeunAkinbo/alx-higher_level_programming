#!/usr/bin/python3

def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        return result
    except (ZeroDivisionError, ValueError, TypeError):
        result = None
        return result
    finally:
        print("Inside result: {:s}".format(str(result)))
