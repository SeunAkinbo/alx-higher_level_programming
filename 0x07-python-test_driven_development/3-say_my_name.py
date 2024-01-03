#!/usr/bin/python3

'''
The Module contains a function that prints the fullname
Module: 3-say_my_name
Function: say_my_name
'''


def say_my_name(first_name, last_name=""):
    '''Prints the <first name> <last name>
    Parameter: first_name and last_name=""
    '''

    '''Validates firstname'''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    '''Validaytes lastname'''
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    '''Prints the fullname'''
    print(f"My name is {first_name} {last_name}")
