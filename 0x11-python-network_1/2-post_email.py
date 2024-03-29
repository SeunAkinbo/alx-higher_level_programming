#!/usr/bin/python3
"""Module: 2-post_email"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys


def postEmail():
    """The function fetches the url response header and displays value"""
    url = sys.argv[1]
    email = sys.argv[2]
    data = urlencode({"email": email})
    data = data.encode('ascii')
    req = Request(url, data)

    with urlopen(req) as response:
        post_email = response.read().decode("utf-8")
        return post_email


if __name__ == "__main__":
    email = postEmail()
    email
