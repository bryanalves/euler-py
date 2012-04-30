#!/usr/bin/env python

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import lib

def euler_21(n):
    return sum([x for x in range(n) if is_amicable(x)])

def is_amicable(n):
    m = sum_divisors(n)
    if (n == m):
        return False

    return sum_divisors(m) == n

def sum_divisors(n):
    return sum(lib.proper_divisors(n))

if __name__ == "__main__":
    print(euler_21(10000))
