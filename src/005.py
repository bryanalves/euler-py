#!/usr/bin/env python

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from functools import reduce

def euler_5(n):
    return reduce(lcm, range(1, n))

def lcm(a, b):
    gcd, tmp = a, b
    while tmp != 0:
        gcd, tmp = tmp, gcd % tmp
    return (a * b) // gcd

if __name__ == "__main__":
    print(euler_5(20))
