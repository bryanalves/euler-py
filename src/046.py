#!/usr/bin/env python

import lib
import itertools

def euler_46():
    r = itertools.count(3, 2)
    composite_odd = filter(lambda x: not lib.is_prime(x), r)

    for n in composite_odd:
        if not any(map(lib.is_prime, (n - s for s in get_squares(n)))):
            return n

def get_squares(n):
    i = 1
    retval = []

    while 2 * (i ** 2) < n:
        retval.append(2 * (i ** 2))
        i += 1

    return retval

if __name__ == "__main__":
    print(euler_46())
