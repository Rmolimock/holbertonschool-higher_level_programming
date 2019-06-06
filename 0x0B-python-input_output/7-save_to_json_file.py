#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    '''writes my_obj to filename as a JSON string'''
    import json
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
