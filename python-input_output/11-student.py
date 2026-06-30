#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the instance."""
        if type(attrs) is list:
            new_dict = {}

            for item in attrs:
                if type(item) is str and item in self.__dict__:
                    new_dict[item] = self.__dict__[item]
            return new_dict

        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes from dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
