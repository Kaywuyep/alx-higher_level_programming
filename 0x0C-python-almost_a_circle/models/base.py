#!/usr/bin/python3
"""a base class module"""
import json


class Base:
    """a first class """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list represented by json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dicts)
                file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            raise ValueError("Unsupported class type")

        dummy_instance.update(**dictionary)
        # Apply real values using update method
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances loaded from a file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
