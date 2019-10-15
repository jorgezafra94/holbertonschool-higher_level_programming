#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Args:
        * obj: object to verify if its class is not a_class class
               and the class of object is an inherited of a_class
        *a_class: class of a object
    Return:
        * True: if class of obj is inheritance of a_class and
                is not a_class
        * False: if is a_class class or is not an inherited one
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
