#!/usr/bin/python3
""" test_indentation(): prints text """


def text_indentation(text):
    """
    Prints a text

    Args:
        text (str): ASCII text
    Exceptions:
        TypeError: If text's type isn't a string
    Return:
        Void
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    new = True
    for char in range(0, len(text)):
        if new is True and text[char] == ' ':
            print(end="")
        elif text[char] == '.' or text[char] == ':' or text[char] == '?':
            print(text[char] + "\n")
            new = True
        else:
            print(text[char], end="")
            new = False
