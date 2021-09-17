#!/usr/bin/python3
"""Documentation for a save_to_json_file function"""

import json

def save_to_json_file(my_obj, filename):
    """Saves a JSON string to a file 
    
    Args:
        my_obj (class object): the object to convert to JSON string
        filename (str): the file to write to
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)