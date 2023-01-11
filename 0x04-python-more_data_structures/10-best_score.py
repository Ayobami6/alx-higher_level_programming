#!/usr/bin/python3
def best_score(my_dict):
    """ get the max value in a dict

    Args:
        my_dict (list): list parsed

    Returns:
        str: the key with max val or none
    """
    if my_dict:
        return max(my_dict, key=my_dict.get)
    else:
        return None
