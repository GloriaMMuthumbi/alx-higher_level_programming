#!/usr/bin/python3
"""
takes url, sends request to url and displays the body
of response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    reqs = requests.get(url)
    if reqs.status_code >= 400:
        print("Error code: {}".format(reqs.status_code))
    else:
        print(reqs.text)
