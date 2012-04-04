#!/usr/bin/env python

"""
The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

        It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

        Which starting number, under one million, produces the longest chain?

        NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def euler_14(maxint):
    arr = [ chaincount(i) for i in range(1, maxint) ]
    return arr.index(max(arr)) + 1

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
def chaincount(n):
    """
    python: 17.253 secs
    pypy: 14.890 secs
    """

    if n == 1:
        return 1

    if n % 2 == 0:
        n >>= 1
    else:
        n = (3 * n) + 1

    return 1 + chaincount(n)

def chaincount2(n):
    """
    python: way too long
    pypy: 7.6 secs
    """

    retval = 1

    while n != 1:
        if n % 2 == 0:
            n >>= 1
        else:
            n = (3 * n) + 1

        retval += 1

    return retval

cache = {}
def chaincount3(n):
    """
    python: 10.769 secs
    pypy: way too long
    """

    retval = 1
    orig = n

    while n != 1:
        if n % 2 == 0:
            n >>= 1
        else:
            n = (3 * n) + 1

        if n in cache.keys():
            cache[orig] = retval + cache[n]
            return cache[orig]

        retval += 1

    cache[orig] = retval
    return retval

if __name__ == "__main__":
    print(euler_14(1000000))
