#!/usr/bin/python3
'''Module:101-add_attribute.py'''


def add_attribute(obj, name, value):
    '''Adds a new attribute to an object if possible

    Args:
        - obj: The object to add the attribute
        - name: The namee of the attribute
        - value: The value of the attribute
    Raises:
        - TypeError: if the object can't have a new attribute
    '''
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
