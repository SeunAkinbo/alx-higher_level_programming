#!/usr/bin/python3
"""Module: 4-hbtn_status"""

import requests


def getStatus(url):
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    res = getStatus(url)
    res
