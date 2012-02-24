#!/usr/bin/env python

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def euler_32():
    pandigitals = []
    pandigitals.extend(pandigital_list(1, 9, 1000, 9999))
    pandigitals.extend(pandigital_list(10, 99, 100, 999))

    result = [a[2] for a in pandigitals]
    print(sum(set(result)))

def pandigital_list(multiplicand_start, multiplicand_end, multiplier_start, multiplier_end):
    retval = []
    for i in range(multiplicand_start, multiplicand_end):
        for j in range(multiplier_start, multiplier_end):
            if is_pandigital(i, j):
                retval.append((i, j, i*j))
    return retval

def is_pandigital(multiplier, multiplicand):
    result = multiplier * multiplicand

    return sorted(str(result) + str(multiplier) + str(multiplicand)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']


euler_32()
