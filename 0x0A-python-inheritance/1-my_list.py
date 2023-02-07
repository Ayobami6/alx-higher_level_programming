#!/usr/bin/python3
""" MyList module
"""


class MyList(list):

    """ Mylist object class that inherit from list builtin
    """

    def print_sorted(self) -> None:
        """ prints sorted list
        """
        print(sorted(self))
