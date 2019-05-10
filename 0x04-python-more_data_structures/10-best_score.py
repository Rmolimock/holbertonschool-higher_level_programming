#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    sum, name = 0, None
    for (key, value) in a_dictionary.items():
        if value > sum:
            sum = value
            name = key
    return name
