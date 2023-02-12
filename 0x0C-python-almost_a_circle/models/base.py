#!/usr/bin/python3
""" Base Module
"""
from typing import Optional


class Base:

    """Base Class

    Attributes:
        id (int): id attr
    """

    __nb_objects = 0

    def __init__(self, id: Optional[int] = None) -> None:
        """ instance init function

        Args:
            id (Optional[int], optional): parsed id arg
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
