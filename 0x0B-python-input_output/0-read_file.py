#!/usr/bin/python3
"""Documentation for read_file location"""

def read_file(filename=""):
    """Function that reads the file and prints its contents to stdout
    
    Args:
        filename (str): the filename to open
    """

    with open(filename, encoding='utf-8') as f:
        for l in f:
            print(l, end="")
            