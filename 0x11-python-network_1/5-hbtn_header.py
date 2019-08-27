#!/usr/bin/python3
# fetch url and display value of x-request-id
import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
