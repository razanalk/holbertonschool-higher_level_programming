#!/usr/bin/python3
"""Module defines BaseGeometry class."""


class BaseGeometry:
    """Base geometry class."""

    def area(self):
        """Raise exception because area is not implemented."""
        raise Exception("area() is not implemented")
