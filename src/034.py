#!/usr/bin/env python

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math

def euler_34():
    #9! * 7 = 2540161, so this is upper limit
    x = range(3, 2540161)
    return sum(filter(factorial_filter, x))

def factorial_filter(x):
    return x == sum([math.factorial(int(y)) for y in str(x)])

if __name__ == "__main__":
    print(euler_34())
