#!/usr/bin/python3
"""Define a function that checks  if the object is an instance of a class \
    that inherited (directly or indirectly) from the specified class
    """


def inherits_from(obj, a_class):
    """
    Function that Returns True if the object is an instance of a class \
    that inherited (directly or indirectly) from the specified class \
    Otherwise return False
    """

    if isinstance(issubclass(type(obj), a_class)):
        return True
    return False
