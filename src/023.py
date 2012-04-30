#!/usr/bin/env python

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import lib

def euler_23():
    return sum(set(range(1,28124)).difference(abundant_sums()))

def abundant_sums():
    a_nums = abundant_nums()
    return set(x + y for x in a_nums for y in a_nums if x + y < 28124)

def abundant_nums():
    return [x for x in range(1,28124) if is_abundant(x)]

def is_abundant(n):
    divisors = lib.proper_divisors(n)
    return sum(set(divisors)) > n

if __name__ == "__main__":
    print(euler_23())
