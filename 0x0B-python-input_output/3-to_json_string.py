#!/usr/bin/python3
'''Module: 3-to_json_string.py'''

import json


def to_json_string(my_obj):
    '''Returns the JSON representation of an object
    Args:
        - my_obj: Python object to be converted to JSON string

    returns: The JSON string representation
    '''
    return json.dumps(my_obj)
