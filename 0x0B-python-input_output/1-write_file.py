#!/usr/bin/python3
"""Documentation for a write_file function"""

def write_file(filename="", text=""):
    """Writes a specified text to a file
    
    Args:
        filename (str): the file to open 
        text (str): the text to write to the file 
    """

    with open (filename, mode='w', encoding='utf-8') as f:
        written = f.write(text)
    return written