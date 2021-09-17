#!/usr/bin/python3
"""Documentation for a load_from_json"""

import json

def load_from_json_file(filename):
    """Takes a JSON string and returns the object from a file
    
    Args: 
        filename (str): the file to load the string from
        
    Returns: 
        the JSON object represented by the string in the file
    """

    with open(filename) as f:
        json_obj = json.load(f)
    return json_obj