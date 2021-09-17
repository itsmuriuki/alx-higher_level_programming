#!/usr/bin/python3
"""Documentation for a to_json_string function"""

import json

def to_json_string(my_obj):
    """Converts an object to a JSON string
    
    Args:
        my_obj (class object): the object to convert to JSON string
    
    Returns:
        The JSON string representation of the object
    """

    return json.dumps(my_obj)
    