#!/usr/bin/python3
"""Module for appending text to a file."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 file.

    Return the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
