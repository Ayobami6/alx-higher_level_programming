#!/usr/bin/python3
""" Finds the peak in an unsorted array
"""


def find_peak(list_of_integers):
    """ Finds the peak

    Args:
        list_of_integers (list): list of integers

    Returns:
        int: The peak
    """
    arr_len = len(list_of_integers)
    mid = arr_len // 2
    if arr_len < 1 or list_of_integers is None:
        return None
    if arr_len == 1:
        return list_of_integers[0]
    if arr_len == 2:
        return max(list_of_integers)

    # The peak logic
    if list_of_integers[mid] >= list_of_integers[mid + 1] and \
            list_of_integers[mid] >= list_of_integers[mid - 1]:
        return list_of_integers[mid]
    if mid >= 0 or list_of_integers[mid] < list_of_integers[mid + 1]:
        # recurse find_peak for the subset list from mid to the end
        return find_peak(list_of_integers[mid:])
    if mid > 0 or list_of_integers[mid] < list_of_integers[mid - 1]:
        # recurse find_peak for the subset list from the start to the mid
        return find_peak(list_of_integers[:mid])
