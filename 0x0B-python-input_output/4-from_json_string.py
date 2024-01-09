#!/usr/bin/python3
'''Module: 4-from_json_string.py'''

import json


def from_json_string(my_str):
    '''Returns an object (Python data structure) represented by a JSON string
    Args:
        - my_str: JSON string
    return: The Python object represented by the JSON string
    '''
    return json.loads(my_str)