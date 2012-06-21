#!/usr/bin/env python

import lib
import itertools

def euler_45():
    triangles = filter(_filter, lib.triangle_gen())
    return next(itertools.islice(triangles, 1))

def _filter(n):
    return n > 40755 and is_hexagonal(n) and lib.is_penta(n)

@lib.memoize
def is_hexagonal(n):
    x = ((((8 * n)  + 1) ** 0.5) + 1) / 4
    try:
        return x == int(x)
    except TypeError:
        return False

if __name__ == "__main__":
    print(euler_45())
