#!/usr/bin/python3
"""Documentation for a class_to_json function"""

def class_to_json (obj):
    """Returns a dictionary representation of an object for JSON serializing
    
    Args: 
        obj (class object): the object to be serialized
    """

    return obj.__dict__
    