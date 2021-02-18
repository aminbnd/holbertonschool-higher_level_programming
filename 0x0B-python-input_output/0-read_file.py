#!/usr/bin/python3
"""
Module containing a function that reads a text file (encoding UTF-8)
and prints it in stdout
"""
def read_file(filename=""):
    """ Function that reads a text file (encoding UTF-8)
and prints it in stdout
"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
