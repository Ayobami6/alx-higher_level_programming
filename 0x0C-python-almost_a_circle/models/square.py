#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size: int, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs) -> None:
        """ Update value method

        Args:
            *args: Tuple of args
            **kwargs: key, value args
        """
        if len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1

        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self) -> str:
        """ magic method overwrite

        Returns:
                str: rectangle description
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def to_dictionary(self) -> dict:
        """ Details to dict

        Returns:
            dict: Dictionary of attr
        """
        dico = dict(id=self.id, size=self.size, x=self.x, y=self.y)
        return dico
