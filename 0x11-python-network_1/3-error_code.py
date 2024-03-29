#!/usr/bin/python3
"""Module: 3-error_code"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import sys


def respErr():
    """The function fetches the url response and checks for error"""
    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(url) as response:
            res = response.read().decode("utf-8")
            return res
    except HTTPError as e:
        print("Error code: {}".format(e.code))
    except URLError as e:
        print("Reason: {}".format(e.reason))


if __name__ == "__main__":
    res = respErr()
    res
