#!/usr/bin/python3
"""
takes url, sends request to it, displays the value of variable
X-Request-Id in the reponse header
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    reqs = request.get(url)
    print(r.headers.get("X-Request-Id'"))
