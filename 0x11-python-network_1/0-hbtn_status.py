#!/usr/bin/python3
"""Module: 0-hbtn_status"""

from urllib.request import Request, urlopen
from urllib.error import URLError


def openUrl(url):
    """The function fetches the url response"""
    req = Request(url)

    try:
        with urlopen(req) as response:
            url_page = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(url_page)))
            print("\t- content: {}".format(url_page))
            print("\t- utf8 content: {}".format(url_page.decode("utf-8")))
    except URLError as e:
        if hasattr(e, "reason"):
            print("Failed to reach server.")
            print("Reason: ", e.reason)
        elif hasattr(e, "code"):
            print("Request execution failed.")
            print("Error coded: ", e.code)


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    the_page = openUrl(url)
    the_page
