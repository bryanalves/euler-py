
def get_max_children(triangle, row, col):
    retval = triangle[row][col]
    if row == len(triangle) - 1:
        return retval 

    return retval + max(
        get_max_children(triangle, row + 1, col),
        get_max_children(triangle, row + 1, col + 1)
    )
