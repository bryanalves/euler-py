#!/usr/bin/env python
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

import itertools
import operator
import functools
import lib

def euler_33():
    nums = range(10, 100)
    dens = range(10, 100)

    fracs = ((n, d) for n, d in itertools.product(nums, dens))
    filtered_fracs = list(filter(cancel_filter, fracs))
    num = functools.reduce(operator.mul, [x[0] for x in filtered_fracs], 1)
    den = functools.reduce(operator.mul, [x[1] for x in filtered_fracs], 1)
    divisor = lib.gcd(num, den)
    return den // divisor

def cancel_filter(x):
    if (x[0] >= x[1]):
        return False
    num = str(x[0])
    den = str(x[1])
    if (num[0] == den[1]):
        return (int(num[1]) / int(den[0])) == x[0] / x[1]
    elif (num[1] == den[0] and den[1] != '0'):
        return (int(num[0]) / int(den[1])) == x[0] / x[1]
    else:
        return False

if __name__ == "__main__":
    print(euler_33())
