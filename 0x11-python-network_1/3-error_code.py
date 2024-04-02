#!/usr/bin/python3
"""
takes url, send request to the url and displays the body of
response decoded in utf-8
"""
import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]

    own_request = request.Request(url)
    try:
        with request.urlopen(own_request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
