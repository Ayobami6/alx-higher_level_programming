#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    """ multiply a list using map to iterate and lambda for action

    Args:
        my_list (list, optional): parsed list. Defaults to [].
        number (int, optional): number arg for action. Defaults to 0.

    Returns:
        list: multiplied list
    """
    return list(map(lambda n: n * number, my_list))
