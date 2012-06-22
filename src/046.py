#!/usr/bin/env python

import lib
import itertools

def euler_46():
    r = itertools.count(3, 2)
    composite_odd = filter(lambda x: not lib.is_prime(x), r)

    for n in composite_odd:
        squares = itertools.takewhile(lambda x: x < n,
                (2 * (i ** 2) for i in itertools.count()))
        if not any(map(lib.is_prime, (n - s for s in squares))):
            return n

if __name__ == "__main__":
    print(euler_46())
