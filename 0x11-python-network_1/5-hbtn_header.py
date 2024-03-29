#!/usr/bin/python3
"""Module: 5-hbtn_header"""

import requests
import sys


def postHead(value):
    url = sys.argv[1]
    response = requests.get(url)
    return response.headers.get(value)


if __name__ == "__main__":
    val = "X-Request-Id"
    res = postHead(val)
    print(res)
