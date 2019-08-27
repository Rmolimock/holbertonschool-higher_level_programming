#!/usr/bin/python3
# send request with parameter, display response as JSON
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        value = sys.argv[1]
    else:
        value = ""
    param = {"q": value}
    response = requests.post(url, param)
    try:
        user = response.json()
        if (len(user) < 1):
            print("No result")
        else:
            print("[{}] {}".format(user["id"], user["name"]))
    except:
        print("Not a valid JSON")
