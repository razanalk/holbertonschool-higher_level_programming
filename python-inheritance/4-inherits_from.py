#!/usr/bin/python3
"""Check if object inherited from a class."""


def inherits_from(obj, a_class):
    """Return True if obj inherited from a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
