#!/usr/bin/python3
"""Module: 7-error_code"""

import requests
import sys


def statusCode():
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        return "Error code: {}".format(response.status_code)
    else:
        return response.text


if __name__ == "__main__":
    res = statusCode()
    print(res)
