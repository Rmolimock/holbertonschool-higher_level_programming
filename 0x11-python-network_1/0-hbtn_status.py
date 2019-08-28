#!/usr/bin/python3
# fetches a url using urllib
from urllib import request


if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as r:
        print('Body response:')
        response = r.read()
        print('\t- type: {}'.format(type(response)))
        print('\t- content: {}'.format(response))
        print('\t- utf8 content: {}'.format(response.decode('utf-8')))
