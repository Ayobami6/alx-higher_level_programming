#!/usr/bin/python3

""" Square class

    """


class Square:
    """ Square class with instance private attr size
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Square class instance initialization

        Args:
            size (int, optional): size of the square. Defaults to 0.
            position (tuple, optional): position of the square object
        """
        self.size = size
        self.position = position

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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """ get the position att

        Returns:
            tuple: the square position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets position values

        Args:
            value (tuple): position of the square

        Raises:
            TypeError: Position must be a tuple with 2 positive int
        """
        if type(value) != tuple or len(value) != 2 or \
           not all([type(i) == int for i in value]) or \
           not all([i >= 0 for i in value]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Area method for the square class

        Returns:
            int: size * size
        """
        return self.__size * self.__size

    def my_print(self):
        """ Prints a square
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
