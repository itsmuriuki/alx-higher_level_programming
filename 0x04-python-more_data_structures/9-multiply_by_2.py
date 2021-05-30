#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = list(a_dictionary.keys())
    new_dictionary = {}
    for i in keys:
        new_dictionary[i] = a_dictionary[i] * 2
    return new_dictionary
