#!/usr/bin/python3
""" read file module
"""


def read_file(filename=""):
    """ read files line by line

    Args:
        filename (str, optional): a text file or a string
    """
    with open(filename,  mode="r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
