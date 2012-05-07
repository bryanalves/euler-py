#!/usr/bin/env python

"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import lib
import itertools

def euler_37():
    primes = lib.prime_gen()

    candidates = itertools.chain(*[itertools.product(['1', '2', '3', '5', '7', '9'], repeat=n) for n in range(2, 11)])

    truncatable_primes = (int(''.join(n)) for n in candidates if is_truncatable_prime((''.join(n))))
    return sum(list(itertools.islice(truncatable_primes, 11)))


def is_truncatable_prime(n):
    if n in ["2", "3", "5", "7"]: return False
    l = len(n)

    for i in range(0, l):
        m = int(n[i:])
        if not lib.is_prime(m): return False

        m = int(n[0:l-i])
        if not lib.is_prime(m): return False

    return True

if __name__ == "__main__":
    print(euler_37())
