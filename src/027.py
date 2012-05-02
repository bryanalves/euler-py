#!/usr/bin/env python
"""
Euler published the remarkable quadratic formula:

    n² + n + 41

    It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

    Using computers, the incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

            n² + an + b, where |a| < 1000 and |b| < 1000

                where |n| is the modulus/absolute value of n
                    e.g. |11| = 11 and |−4| = 4

                    Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

import lib
import itertools
import operator

def euler_27(max_a, max_b):
    a = range(-max_a, max_a + 1)
    #n = 0 means that the equation simplifies to b, so b must be prime.
    b = filter(lambda x: lib.is_prime(abs(x)), range(-max_b, max_b + 1))

    vars = filter(a_filter, itertools.product(a, b))
    solution = max((consec_primes_for_eq(*var), var) for var in vars)[1]
    return operator.mul(*solution)

def a_filter(inp):
    """
    When n == 1 the equation is 1 + a + b. Since we want primes here, we need an odd number.  So if b is even, a must be even, otherwise a must be odd.  This lets us filter out lots of as.
    """
    a, b = inp
    if b % 2 == 0:
        return a % 2 == 0
    else:
        return a % 2 != 0

def consec_primes_for_eq(a, b):
    n = 0
    while lib.is_prime(abs((n * n) + (a * n) + b)):
        n += 1

    return n


if __name__ == "__main__":
    print(euler_27(1000, 1000))
