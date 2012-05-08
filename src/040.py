#!/usr/bin/env python
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

import itertools
import operator
import functools

def euler_40():
    gen = (int(y) for x, y in enumerate(sequence_gen()) if x + 1 in [1, 10, 100, 1000, 10000, 100000, 1000000])
    return functools.reduce(operator.mul, itertools.islice(gen, 7), 1)

def sequence_gen():
    i = itertools.count(1)
    for x in i:
        for y in str(x):
            yield y

if __name__ == "__main__":
    print(euler_40())
