#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(sorted((a_dictionary.keys())))
    for i in keys:
        print("{}: {}".format(i, a_dictionary[i]))
