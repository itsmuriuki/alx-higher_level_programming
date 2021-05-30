#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    keys = list(a_dictionary.keys())
    maxi = keys[0]
    for i in keys:
        maxi = i if a_dictionary[i] > a_dictionary[maxi] else maxi
    return maxi
