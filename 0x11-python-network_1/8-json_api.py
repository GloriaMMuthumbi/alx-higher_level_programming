#!/usr/bin/python3
"""
sends post request to http://0.0.0.0:5000/search_user with letter
as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    pl = {"q": letter)

    reqs = requests.post("http://0.0.0.0:5000/search_user", data=pl)
    try:
        reponse = reqs.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(repsonse.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
