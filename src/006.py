#!/usr/bin/env python

"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def euler_6(n):
    return (square_of_sum(n) - sum_of_square(n))

def square_of_sum(n):
    return pow(sum(range(n + 1)), 2)

def sum_of_square(n):
    return sum((x * x for x in range(n + 1)))

if __name__ == "__main__":
    print(euler_6(100))
