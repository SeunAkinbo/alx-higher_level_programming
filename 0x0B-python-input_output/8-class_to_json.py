#!/usr/bin/python3
'''Module: 8-class_to_json.py'''


def class_to_json(obj):
    '''Returns the dictionary description with simple data structure
    Args:
        - obj
    return: Dictionary description
    '''
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
