#!/usr/bin/python3
"""Define Locked Class"""


class LockedClass:
    """A class that prevents the user from dynamically creating new attributes except 'first_name'."""

    __slots__ = ["first_name"]
