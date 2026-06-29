#!/usr/bin/python3
"""Module for JSON serialization."""

import json


def to_json_string(my_obj):
    """Return the JSON representation of an object."""
    return json.dumps(my_obj)
