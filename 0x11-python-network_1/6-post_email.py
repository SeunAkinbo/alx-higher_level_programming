#!/usr/bin/python3
"""Module: 6-post_email"""

import requests
import sys


def postEmail():
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}
    response = requests.post(url, data=data)
    return response.text


if __name__ == "__main__":
    res = postEmail()
    print(res)
