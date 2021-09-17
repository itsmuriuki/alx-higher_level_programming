#!/usr/bin/python3
"""Documentation for a from_json_string function"""

import json

def from_json_string(my_str):
    """Converts a JSON string to an object
    
    Args:
        my_str (seralized str): the string to convert to object

    Returns:
        the deserialized string 
    """
    return json.loads(my_str)
