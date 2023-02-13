#!/usr/bin/python3
""" Base Module
"""
from typing import Optional
import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts dicts to json to the data

        Args:
            list_dictionaries (list): list of dicos

        Returns:
            json: dumped json
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save json to file

        Args:
            list_objs (list): List of objects
        """
        filename = cls.__name__+".json"
        with open(filename, mode="w") as file:
            if list_objs == None:
                file.write("[]")
            else:
                dict_list = []
                for obj in list_objs:
                    dict_list.append(obj.to_dictionary())
                file.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """ load from json string

        Args:
            json_string (dict strin): Description

        Returns:
            json: Retreived dict
        """
        if json_string == None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create new instance dictionary

        Args:
            **dictionary: dictionary

        Returns:
            dict: new instance dict
        """
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(2, 3)
            else:
                new_instance = cls(2)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """ Load from file

        Returns:
            list: list of dict
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r") as file:
                dict_list = Base.from_json_string(file.read())
                return [cls.create(**item) for item in dict_list]
        except IOError:
            return []
