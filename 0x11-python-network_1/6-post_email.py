#!/usr/bin/python3
"""
takes in url and email address, sends post request to url with
the email as paramaeter and displays body of the response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    reqs = requests.post(url, data={"email": email})
    print(reqs.text)
