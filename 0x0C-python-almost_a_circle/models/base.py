#!/usr/bin/python3
"""This module defines class Base."""

import json
import csv


class Base:
    """base of all other classes of this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initiliazes id"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=None):
        """returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON string representation of list_objes to a file."""
        filename = cls.__name__ + ".json"
        list_dictionaries = []
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                for instance in list_objs:
                    list_dictionaries.append(instance.to_dictionary(instance))
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string."""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1, 0, 0)
        if cls.__name__ == "Square":
            instance = cls(1, 0, 0)
        else:
            instance = cls()
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        results = []
        try:
            with open(filename, 'r') as f:
                for instance in cls.from_json_string(f.read()):
                    results.append(cls.create(**instance))
        except Exception as err:
            pass
        return results

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and writes to CSV file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for instance in list_objs:
                writer.writerow(instance.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes and returns a list of instances fro CSV file."""
        filename = cls.__name__ + ".csv"
        results = []
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    results.append(cls.create_from_csv_row(row))
        except FileNotFoundError:
            pass
        return results

    def to_csv_row(self):
        """Returns a CSV row"""
        raise NotImplementedError("to_csv_row method must be implemented")

    @classmethod
    def create_from_csv_row(cls, csv_row):
        """Creates an instance from a CSV row."""
        raise NotImplementedError("create_from_csv_row method must be implemented")


