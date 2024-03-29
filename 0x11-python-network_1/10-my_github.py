#!/usr/bin/python3
"""Module: 10-my_github"""

import requests
import sys


def logMeIn():
    """The function retrives the user ID with the
    GitHub credentials provided
    """

    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    return response.json().get('id')


if __name__ == "__main__":
    res = logMeIn()
    print(res)
