#!/usr/bin/env python

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def euler_4():
    palindromes = []
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            x = i * j
            if is_palindrome(x):
                palindromes.append(x)
    return palindromes

def is_palindrome(x):
    x_s = str(x)
    return x_s == x_s[::-1]

if __name__ == "__main__":
    print(max(euler_4()))
