#!/usr/bin/python3
"""base class module"""
import json


class Base:
    """Base Class defined"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes class instance"""
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects

    @property
    def id(self):
        """returns instance id"""
        return self.__id

    @id.setter
    def id(self, value):
        """sets instance id"""
        self.__id = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of an object (string)"""
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = str(cls.__name__) + ".json"
        dict1 = []
        if list_objs is not None:
            for i in list_objs:
                dict1.append(i.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dict1))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        dict = []
        if json_string:
            dict = json.loads(json_string)
        return dict

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            c1 = cls(1, 1)
        else:
            c1 = cls(1)
        c1.update(**dictionary)
        return c1

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = str(cls.__name__) + ".json"
        instance_list = []
        try:
            with open(filename, "r", encoding="utf-8") as my_file:
                dict_from_file = cls.from_json_string(my_file.read())

                for dictionary in dict_from_file:
                    instance_list.append(cls.create(**dictionary))

                return instance_list
        except FileNotFoundError:
            return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes in CSV, similar to save_to_file(json) """
        filename = str(cls.__name__) + ".csv"
        with open(filename, "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            dict_list = []
            if list_objs is None:
                csv_writer.writerow(dict_list)
            else:
                for obj in list_objs:
                    for key, value in obj.to_dictionary().items():
                        dict_list.append(value)
                    csv_writer.writerow(dict_list)
                    dict_list = []

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in CSV, similar to from_file(json) """
        filename = str(cls.__name__) + ".csv"
        instance_list = []
        if filename is None:
            return instance_list
        else:
            with open(filename, "r", encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file)
                if cls.__name__ == "Rectangle":
                    attrs = ['id', 'width', 'height', 'x', 'y']
                if cls.__name__ == "Square":
                    attrs = ['id', 'size', 'x', 'y']

                for row in csv_reader:
                    attr_dict = {attrs: int(row)
                                 for attrs, row in zip(attrs, row)}
                    instance_list.append(cls.create(**attr_dict))

            return instance_list
