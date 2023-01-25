#!/usr/bin/python3
"""
Square class
"""


class Square:
    """A class that defines a square by size and can compute area"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ get size attr with property decorator

        Returns:
            int: the size value
        """
        return self.__size

    @size.setter
    def size(self, size):
        """ Square class instance initialization

         Args:
             size (int): size of square.

         Raises:
             TypeError: size must be an integer
             ValueError: size must not be less than 0
         """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __lt__(self, other):
        """ less than attr that helps to compare two instances

        Args:
            other (class object): class instance

        Returns:
            boolean: True or False
        """
        return self.__size < other.size

    def __le__(self, other):
        """ less than or equal magic method that helps to compare two instances

        Args:
            other (class object): class instance

        Returns:
            bool: True or False
        """
        return self.__size <= other.size

    def __eq__(self, other):
        """ equal to method that helps to compare two instances

        Args:
            other (class object): class instance

        Returns:
            bool: True or False
        """
        return self.__size == other.size

    def __ne__(self, other):
        """ not equal to method that helps to compare two instances

        Args:
            other (class object): class instance

        Returns:
            bool: True or False
        """
        return self.__size != other.size

    def __gt__(self, other):
        """ greater than method that helps to compare two instances

        Args:
            other (class object): class instance

        Returns:
            bool: True or False
        """
        return self.__size > other.size

    def __ge__(self, other):
        """ greater or equal than method that helps to compare two instances

        Args:
            other (class object): class instance

        Returns:
            bool: True or False
        """
        return self.__size >= other.size
