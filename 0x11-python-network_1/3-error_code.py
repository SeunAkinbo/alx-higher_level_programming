#!/usr/bin/python3
"""Module: 3-error_code"""

from urllib.request import Request, urlopen
from urllib.error import URLError
import sys


def respErr():
    """The function fetches the url response and checks for error"""
    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            res = response.read().decode("utf-8")
            return res
    except URLError as e:
        if hasattr(e, "reason"):
            print("Failed to reach server.")
            print("Reason: ", e.reason)
        elif hasattr(e, "code"):
            print("Request execution failed.")
            print("Error code: ", e.code)


if __name__ == "__main__":
    res = respErr()
    res
