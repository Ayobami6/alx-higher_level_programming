#!/usr/bin/python3
""" Lookup module
"""


def lookup(obj: object) -> list:
    """ gets all methods associated with the object

    Args:
        obj (object): Description

    Returns:
        list: list of methods
    """
    return dir(obj)
