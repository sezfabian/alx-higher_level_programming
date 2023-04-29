#!/usr/bin/python3
"""
script takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    req = Request(argv[1])

    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
