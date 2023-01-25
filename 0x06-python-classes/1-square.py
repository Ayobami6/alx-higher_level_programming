#!/usr/bin/python3

"""
    This is a square class module
"""


class Square:
    """ Square object with size private instance attr
    """

    def __init__(self, size):
        """ Square class instance initialization

        Args:
            size (int): size of the square
        """
        self.__size = size
