#!/usr/bin/python3
""" Write text file (UTF-8)"""


def write_file(filename="", text=""):
    """ Function that writes a text
    Args:
        filename (str) : the name of the file
        text (str): text to write
    Return: Number of characters written
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
