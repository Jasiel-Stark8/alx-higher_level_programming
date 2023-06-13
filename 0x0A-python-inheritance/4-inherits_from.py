#!/usr/bin/python3
"""Define a function that checks  if the object is an instance of a class \
    that inherited (directly or indirectly) from the specified class
    """


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.
    Otherwise, it returns False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False

"""
Here's an explanation of the modified code:

The code defines a function named `inherits_from` that 
checks if an object is an instance of a class that inherited 
(directly or indirectly) from the specified class.

1. The function `inherits_from` takes two parameters: `obj` 
(the object to check) and `a_class` (the specified class).

2. The `issubclass()` function is used to check if the type of `obj` 
(i.e., `type(obj)`) is a subclass of `a_class`.

3. The `isinstance()` function is not needed in this case since the 
goal is to check for inheritance rather than direct instantiation.

4. The condition `type(obj) is not a_class` ensures that the object 
is not an exact instance of `a_class`. It avoids returning `True` if `obj` 
is an exact instance of `a_class` but not a subclass.

5. If the condition is met, the function returns `True`, indicating 
that `obj` is an instance of a class that inherited from `a_class`. 
Otherwise, it returns `False`.

This implementation correctly checks if the object is an instance of 
a class that inherited (directly or indirectly) from the specified class.
"""
