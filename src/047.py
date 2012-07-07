#!/usr/bin/env python

import lib
from collections import defaultdict
import itertools

def euler_47():
    i = itertools.count()
    consecutive = 0
    while True:
        n = next(i)
        if len(prime_factors(n).keys()) >= 4:
            consecutive += 1
            if consecutive == 1:
                possible_retval = n

            if consecutive == 4:
                return possible_retval
        else:
            consecutive = 0

pregenned_primes = []
primes = lib.prime_gen()

def prime_factors(n):
    retval = defaultdict(int)

    for p in pregenned_primes:
        while n % p == 0:
            n /= p
            retval[p] += 1
            if n == 1:
                return retval

    while n > 1:
        p = next(primes)
        pregenned_primes.append(p)
        while n % p == 0:
            n /= p
            retval[p] += 1

    return retval

if __name__ == "__main__":
    print(euler_47())
