#!/usr/bin/python3

""" Square class

    """


class Square:
    """ Square class with instance private attr size
    """

    def __init__(self, size=0):
        """ Square class instance initialization

         Args:
             size (int, optional): size of square. Defaults to 0.

         Raises:
             TypeError: size must be an integer
             ValueError: size must not be less than 0
         """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Area method for the square class

        Returns:
            int: size * size
        """
        return self.__size * self.__size
