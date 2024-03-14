#!/usr/bin/python3
'''A function that returns True if the object is
an instance of a class that inherited (directly or indirectly)'''


def inherits_from(obj, a_class):
    '''Function to check if the object is an instance of a class
    that inherited (directly or indirectly)

    Args:
        obj: the object
        a_class: the class

    Returns:
        True: if the object is an instance of a subclass
        False: if the object isn't an instance of a subclass
    '''
    return isinstance(obj, a_class) and type(obj) != a_class
