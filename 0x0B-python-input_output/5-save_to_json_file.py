#!/usr/bin/python3
'''Module: 5-save_to_json_file.py'''

import json


def save_to_json_file(my_obj, filename):
    '''Writes an object to a text file, using JSON representation
    Args:
        - my_obj: Object string representation
        - filename: The file path
    '''
    with open(filename, "w") as my_file:
        json.dump(my_obj, my_file)
