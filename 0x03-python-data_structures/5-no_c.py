#!/usr/bin/python3
def no_c(my_string):
    new_string = [i for i in my_string if i != 'c' and i != 'C']
    new_string = ''.join(new_string)
    return new_string
