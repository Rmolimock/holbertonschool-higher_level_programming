#!/usr/bin/python3
def from_json_string(my_str):
    '''Returns an object from a JSON string'''
    import json
    return json.loads(my_str)
