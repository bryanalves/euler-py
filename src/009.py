#!/usr/bin/env python

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from itertools import combinations_with_replacement

def euler_9(m):
    return [x[0] * x[1] * x[2] for x in pythagorean_gen(m // 2) if sum(x) == m][0]

def pythagorean_gen(m):
    gen = combinations_with_replacement(range(1, m), 2)
    for a, b in gen:
        c = ((a ** 2) + (b ** 2)) ** 0.5
        if c == int(c):
            yield (a, b, int(c))

if __name__ == "__main__":
    print(euler_9(1000))
