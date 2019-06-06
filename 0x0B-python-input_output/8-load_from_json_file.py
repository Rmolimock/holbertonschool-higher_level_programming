#!/usr/bin/python3
def load_from_json_file(filename):
    '''Load an object from a JSON file'''
    import json
    with open(filename, mode="r") as f:
        return json.load(f)
