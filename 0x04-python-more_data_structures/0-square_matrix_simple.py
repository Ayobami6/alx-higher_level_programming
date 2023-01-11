#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """squares the element of a matrix

    Args:
        matrix (list, optional): 2D list. Defaults to [].
    Returns:
        new_list: new 2D list
    """
    new_list = []
    for i in range(len(matrix)):
        new_list.append(list(map(lambda x: x**2, matrix[i])))
    return new_list
