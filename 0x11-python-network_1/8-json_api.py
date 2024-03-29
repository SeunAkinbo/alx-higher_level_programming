#!/usr/bin/python3
"""Module: 8-json_api"""

import requests
import sys


def jsonAPI(url):
    """The function that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter
    as a parameter
    """
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    data = {"q": letter}
    response = requests.post(url, data=data)
    res_type = response.headers["content-type"]

    if res_type == "application/json":
        obj = response.json()
        if obj:
            return "[{}] {}".format(data['id'], data['name'])
        else:
            return "No result"
    else:
        return "Not a valid JSON"


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    res = jsonAPI(url)
    print(res)
