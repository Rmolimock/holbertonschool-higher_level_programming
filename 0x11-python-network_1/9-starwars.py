#!/usr/bin/python3
# acces star wars api and print name containing r2
import sys
import requests

if __name__ == "__main__":
    search = sys.argv[1]
    url = "https://swapi.co/api/people" + "?search=" + search
    response = requests.get(url)
    json_format = response.json()
    print("Number of results: " + str(json_format['count']))
    for ret_dict in json_format['results']:
        print(ret_dict['name'])
