#!/usr/bin/python3
# access github API and print user id
import requests
import sys
from requests.auth import HTTPBasicAuth

credentials = HTTPBasicAuth(sys.argv[1], sys.argv[2])
response = requests.get('http://api.github.com/user', auth=credentials)
print(response.json()['id'])
