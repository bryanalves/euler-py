#!/usr/bin/env python
"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros
"""

import lib

def euler_36(m):
    solution = [x for x in range(1, m, 2) if lib.is_palindrome(x) and is_palindrome_base_2(x)]
    return sum(solution)

def is_palindrome_base_2(n):
    return lib.is_palindrome(bin(n)[2::])

if __name__ == "__main__":
    print(euler_36(1000000))
