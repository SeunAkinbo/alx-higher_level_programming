#!/usr/bin/python3
"""Module: 1-hbtn_header"""

from urllib.request import Request, urlopen
from urllib.error import URLError
import sys


def getHeader(value):
    """The function fetches the url response header and displays value"""
    req = Request(sys.argv[1])

    try:
        with urlopen(req) as response:
            head = response.headers[value]
            return head
    except URLError as e:
        if hasattr(e, "reason"):
            print("Failed to reach server.")
            print("Reason: ", e.reason)
        elif hasattr(e, "code"):
            print("Request execution failed.")
            print("Error coded: ", e.code)


if __name__ == "__main__":
    value = "X-Request-Id"
    head = getHeader(value)
    print(head)
