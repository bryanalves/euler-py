#!/usr/bin/env python

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def euler_1(n):
    return sum(a for a in range(n) if a % 3 == 0 or a % 5 ==0)

if __name__ == "__main__":
    print(euler_1(1000))
