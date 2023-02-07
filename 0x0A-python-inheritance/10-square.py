#!/usr/bin/python3
""" Square Module

Attributes:
    Rectangle (object): Base Object
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """ Square Class
    """

    def __init__(self, size: int) -> None:
        """ instance initialization function

        Args:
            size (int): Description
        """
        super().__init__(size, size)
