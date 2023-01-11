#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """searches for element in a list and replace

    Args:
        my_list (list): list of data
        search (any): element of any data type
        replace (any): value of any type

    Returns:
        list: new list
    """
    count = 0
    new_list = my_list.copy()
    for i in new_list:
        if i == search:
            new_list[count] = replace
        count = count + 1

    return new_list
