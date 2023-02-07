#!/usr/bin/python3
"""  Add attr module
"""


def add_attribute(obj, a, v):
    """ Adds attr to an object

    Args:
        obj (object): object
        a (str): attr arg
        v (str): attr arg

    Raises:
        TypeError: can't add new attribute
    """
    res = getattr(obj, "__doc__", None)
    if res is None:
        setattr(obj, a, v)
    else:
        raise TypeError("can't add new attribute")
