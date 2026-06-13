#!/usr/bin/python3
"""Module that defines say_my_name"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    name = first_name if last_name == "" else "{} {}".format(
        first_name, last_name
    )
    print("My name is {}".format(name))
