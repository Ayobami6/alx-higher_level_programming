#!/usr/bin/python3
def element_at(my_list, idx):
    """ gets element at a particular index
    of a list

    Args:
        my_list (list): list item
        idx (int): int number

    Returns:
        item: item
    """
    if (0 <= idx < len(my_list)):
        return my_list[idx]
    return None
