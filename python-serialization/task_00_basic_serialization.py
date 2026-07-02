#!/usr/bin/python3

import json


def serialize_and_save_to_file(data, filename):
    """Serialize dictionary to JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON file and return dictionary."""
    with open(filename, "r") as f:
        return json.load(f)
