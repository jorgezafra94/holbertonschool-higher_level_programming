#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Args:
        * obj: object to verify
        * a_class: if obj class is a_class or is a inherited class of
                   a_class
    Return:
        * True: if it belong to the class a_class or a inherited class of this
        * False: if not
    """
    if isinstance(obj, a_class):
        return True
    return False
