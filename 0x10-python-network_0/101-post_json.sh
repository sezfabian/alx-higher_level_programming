#!/bin/bash
# script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
