#!/usr/bin/python3
# access github API and print user id
import requests
import sys

credentials = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
response = requests.get('http://api.github.com/user', auth=credentials)
try:
    print(response.json()['id'])
except KeyError:
    print("None")
