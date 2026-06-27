#!/usr/bin/python3
"""Mixins"""


class SwimMixin:
    """Swim mixin"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Fly mixin"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class"""

    def roar(self):
        print("The dragon roars!")
