#!/usr/bin/python3
"""Rectangle module."""


class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Print rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rows = []
        for i in range(self.__height):
            rows.append("#" * self.__width)
        return "\n".join(rows)

    def __repr__(self):
        """Return string representation for eval()."""
        return "Rectangle({}, {})".format(
            self.__width,
            self.__height
        )

    def __del__(self):
        """Called when instance is deleted."""
        print("Bye rectangle...")
