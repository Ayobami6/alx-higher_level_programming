#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all the distinct values

    Args:
        my_list (list, optional): parsed list. Defaults to [].

    Returns:
        result: integer result
    """
    new_set = set(my_list)
    new_list = list(new_set)
    result = sum(new_list)
    return result
