#!/usr/bin/python3
# 0-read_file.py
"""Finding a list of available attributes and methods of an object."""


def lookup(obj):
    """Returns that list of attributes and methods.

    Args:

    - obj: object to look into

    """

    return dir(obj)
