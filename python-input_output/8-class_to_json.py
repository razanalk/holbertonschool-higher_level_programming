#!/usr/bin/python3
"""Returns the dictionary description for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
