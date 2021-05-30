#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    for i in keys:
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
