#!/usr/bin/python3
'''Module: 6-load_from_json_file.py'''

import json


def load_from_json_file(filename):
    '''Creates an object from a json file
    Args:
        - filename: JSON file
    '''
    with open(filename, "r") as file:
        json.load(file)
