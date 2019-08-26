#!/usr/bin/python3
# send a post request to a url email and display body of the response
import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == "__main__":
    url = sys.argv[1]
    email = urlencode({'email': sys.argv[2]})
    content = email.encode('ascii')
    post = Request(url, content)

    with urlopen(post) as request:
        response = request.read()
    print(response.decode("utf-8"))
