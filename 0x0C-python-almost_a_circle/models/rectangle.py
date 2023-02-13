#!/usr/bin/python3
""" Rectangle Module
"""
from models.base import Base


class Rectangle(Base):

    """ Rectangle class
    """

    def __init__(self, width: int, height: int, x=0, y=0, id=None) -> None:
        """ Instance init function

        Args:
                width (int): width of rectangle
                height (int): height
                x (int, optional): x of rec
                y (int, optional): y
                id (None, optional): id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self) -> int:
        """ width getter

        Returns:
                int: the width
        """
        return self.__width

    @width.setter
    def width(self, value) -> None:
        """ width setter

        Args:
                value (int): width value

        Raises:
                TypeError: width must be an integer
                ValueError: must be > 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self) -> int:
        """ height getter

        Returns:
                int: the height
        """
        return self.__height

    @height.setter
    def height(self, value) -> None:
        """height setter

        Args:
                value (int): height value

        Raises:
                TypeError: height must be an integer
                ValueError: must be > 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self) -> int:
        """ x getter

        Returns:
                int: x value
        """
        return self.__x

    @x.setter
    def x(self, value) -> None:
        """ x setter

        Args:
                value (int): x value

        Raises:
                TypeError: x must be an integer
                ValueError: x must be >= 0
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self) -> int:
        """ y getter

        Returns:
                int: y value
        """
        return self.__y

    @y.setter
    def y(self, value) -> None:
        """y setter

        Args:
                value (int): y value

        Raises:
                TypeError: y must be an integer
                ValueError: y must be >= 0
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self) -> int:
        """ finds the area of the rectangle

        Returns:
                int: the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """ display the rectangle using #
        """
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(self.y):
            print("")
        for i in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            print("#" * self.width, end="")
            print("")

    def __str__(self) -> str:
        """ magic method overwrite

        Returns:
            str: rectangle description
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs) -> None:
        """ Update rectangle

        Args:
            *args: tuple of args
            **kwargs: keywords args, key and value arguments
        """
        if len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1

        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self) -> dict:
        """ Details to dict

        Returns:
            dict: Dictionary of attr
        """
        dico = dict(id=self.id, width=self.width,
                    height=self.height, x=self.x, y=self.y)
        return dico
