#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    reqs = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print"\t- type: {}".format(type(reqs.text)))
    print("\t- content: {}".format(reqs.text))
