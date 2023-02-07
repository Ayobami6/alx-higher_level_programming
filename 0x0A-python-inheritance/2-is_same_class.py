#!/usr/bin/python3
""" is same class module
"""


def is_same_class(obj: object,  a_class: object) -> bool:
    """ checks if two objects are the same

    Args:
        obj (object): object arg
        a_class (object): object arg

    Returns:
        bool: Description
    """
    return type(obj) == a_class
