#!/usr/bin/env python
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import lib
import itertools

def euler_35(m):
    primes = itertools.takewhile(lambda x: x < m, (n for n in lib.prime_gen()))
    circular_primes = filter(circular_filter, primes)
    return len(list(circular_primes))

def circular_filter(n):
    return all((lib.is_prime(x) for x in rotate_gen(n)))

def rotate_gen(n):
    for i in range(1, len(str(n))):
        n = str(n)
        n = n[1::] + n[0]
        yield int(n)

if __name__ == "__main__":
    print(euler_35(1000000))
