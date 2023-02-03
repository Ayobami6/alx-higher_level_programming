matrix = [[1, 2, 3], [2, 4, 4], [5, 5, 5]]

# sum_list = [sum(x) for x in mat]


def sort_desc(mat: list) -> list:
    """ Sorts a list in descending order

    Args:
        mat (list): paresd list

    Returns:
        list: A new list
    """
    new_list = []
    while mat != []:
        maxx = max(mat)
        new_list.append(maxx)
        mat.remove(maxx)
    return new_list


print(sort_func(matrix))

# start = input("start?: ")

# if start == "Y":
#     print("continue")
