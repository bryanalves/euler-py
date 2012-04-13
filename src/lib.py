
def memoize(function):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            val = function(*args)
            cache[args] = val
            return val
    return decorated_function

def get_max_children(triangle, row, col):
    retval = triangle[row][col]
    if row == len(triangle) - 1:
        return retval 

    return retval + max(
        get_max_children(triangle, row + 1, col),
        get_max_children(triangle, row + 1, col + 1)
    )

