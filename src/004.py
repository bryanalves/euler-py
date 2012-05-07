#!/usr/bin/env python

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import lib

def euler_4():
    palindromes = []
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            x = i * j
            if lib.is_palindrome(x):
                palindromes.append(x)
    return palindromes

if __name__ == "__main__":
    print(max(euler_4()))
