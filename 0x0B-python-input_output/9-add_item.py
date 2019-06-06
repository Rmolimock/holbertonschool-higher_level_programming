#!/usr/bin/python3
"""store arguments to main as elements in list
and save list as JSON file
"""
import sys


serial = __import__('7-save_to_json_file').save_to_json_file
deserial = __import__('8-load_from_json_file').load_from_json_file
f = "add_item.json"
try:
    obj = deserial(f)
except:
    obj = []
# switch prevents the first arg to main (self) from being appended to the list
switch = True
for i in sys.argv:
    if switch is False:
        obj.append(i)
    switch = False
try:
    serial(obj, f)
except:
    pass
