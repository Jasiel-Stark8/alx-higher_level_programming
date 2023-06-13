#!/usr/bin/python3
"""
    Define a function that checks if an object is either and instance of \
    a local class or an inherited class
    """


def is_kind_of_class(obj, a_class):
    """
    Check is obj is an instance of a class or a subclass
    RULE: wrap issubclass first argument 'obj' in type()
    """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False


"""
Here `obj` was being passed directly to the `issubclass()` function. \
However, the `issubclass()` function expects the first argument to be a class (i.e., a type), \
not an instance of a class.

To address this, use the `type()` function on `obj` before passing it to `issubclass()`. \
The `type()` function returns the type of an object, which is the class it belongs to. By using `type(obj)`, \
we ensure that we are passing the class itself to `issubclass()` rather than an instance.

With this modification, the `issubclass()` function will receive the class (type) of `obj` as the first argument, \
allowing it to correctly check if it is a subclass of `a_class`.

In summary, the `type(obj)` change ensures that the `issubclass()` function receives the appropriate argument type, \
which is the class itself rather than an instance, enabling the correct evaluation of whether `obj` is a subclass of `a_class`.
"""
