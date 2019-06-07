#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    '''Insert line into file after given string'''
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.readlines()
    for i, line in enumerate(text):
        if search_string in line:
            text.insert(i + 1, new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        text = "".join(text)
        f.write(text)
