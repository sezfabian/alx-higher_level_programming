#!/usr/bin/python3
"""
script takes in a URL and an email, sends a POST request to the passed URL with
email as a parameter, and displays the body of the response decoded in utf-8
"""
import requests
from sys import argv


if __name__ == "__main__":
    values = {'email': argv[2]}
    req = requests.post(argv[1], values)
    print(req.text)
