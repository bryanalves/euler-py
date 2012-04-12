#!/usr/bin/env python
"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

def euler_16():
    digits = (int(a) for a in str(2 ** 1000))
    return sum(digits)

if __name__ == "__main__":
    print(euler_16())
