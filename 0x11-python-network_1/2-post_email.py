#!/usr/bin/python3
"""Module: 2-post_email"""

from urllib.request import Request, urlopen
from urllib.error import URLError
from urllib.parse import urlencode
import sys


def postEmail():
    """The function fetches the url response header and displays value"""
    url = sys.argv[1]
    email = sys.argv[2]
    data = urlencode({"email": email}).encode('ascii')
    req = Request(url, data=data, method='POST')

    try:
        with urlopen(req) as response:
            post_email = response.read().decode("utf-8")
            return post_email
    except URLError as e:
        if hasattr(e, "reason"):
            print("Failed to reach server.")
            print("Reason: ", e.reason)
        elif hasattr(e, "code"):
            print("Request execution failed.")
            print("Error coded: ", e.code)


if __name__ == "__main__":
    email = postEmail()
    email
