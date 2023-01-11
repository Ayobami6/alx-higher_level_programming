#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    """deletes key value pair from  dict

    Args:
        my_dict (_type_): parsed dict
        key (str, optional): dict key arg. Defaults to "".

    Returns:
        dict: my_dict
    """
    my_dict.pop(key, None)
    return my_dict
