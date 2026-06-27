#!/usr/bin/python3
"""CountedIterator"""


class CountedIterator:
    """Iterator that counts iterations"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        return self.counter
