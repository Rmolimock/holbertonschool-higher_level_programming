#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    sum = 0
    for key in a_dictionary.keys():
        if a_dictionary[key] > sum:
            sum = a_dictionary[key]
    return sum
