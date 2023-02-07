#!/usr/bin/python3
""" is kind of class module
"""


def is_kind_of_class(obj: object, a_class: object) -> bool:
    """ is kind of class function, that checks if two objects are
        from the same class

        Args:
            obj (object): object arg to compare
            a_class (object): object arg

        Returns:
            bool: True or false
        """
    return isinstance(obj, a_class)
