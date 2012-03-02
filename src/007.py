#!/usr/bin/env python

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import itertools

def euler_7(n):
    return next(itertools.islice(prime_gen(), n, None));

def prime_gen():
    n = 2
    while True:
        if is_prime(n):
            yield n

        n += 1

def is_prime(n):
    if n == 2:
        return True

    if not n & 1:
        return False

    for i in range(3, int((n ** 0.5)) + 1, 2):
        if n % i == 0:
            return False

    return True

if __name__ == "__main__":
    print(euler_7(10001))

