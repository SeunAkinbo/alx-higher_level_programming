#!/usr/bin/python3
"""Module: 100-github_commits"""

import requests
import sys


def getCommits():
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)

    objs = response.json()
    x = 0
    while x < 10:
        encrypt_id = objs[x].get("sha")
        author = objs[x].get("commit").get("author").get("name")
        print("{}: {}".format(encrypt_id, author))
        x += 1


if __name__ == "__main__":
    res = getCommits()
    res
