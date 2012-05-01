def proper_divisors(n):
    retval = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            retval.append(i)
            retval.append(n // i)

    return retval

def gcd(a, b):
    gcd, tmp = a, b
    while tmp != 0:
        gcd, tmp = tmp, gcd % tmp

    return gcd

def prime_gen():
    yield 2
    n = 3
    while True:
        if is_prime(n):
            yield n

        n += 1

def lcm(a, b):
    return (a * b) // gcd(a,b)

def fib_gen(a, b):
    while True:
        yield a
        a, b = b, a + b

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

@memoize
def is_prime(n):
    if not n & 1:
        return False

    for i in range(3, int((n ** 0.5)) + 1, 2):
        if n % i == 0:
            return False

    return True


class Triangle:
    def __init__(self, triangle):
        self.triangle = triangle

    @memoize
    def get_max_children(self, row, col):
        retval = self.triangle[row][col]
        if row == len(self.triangle) - 1:
            return retval

        return retval + max(
            self.get_max_children(row + 1, col),
            self.get_max_children(row + 1, col + 1)
        )

