#!/usr/bin/env python
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def euler_20(fact):
    acc = fact
    while fact > 1:
        fact -= 1
        acc *= fact

    return sum([int(x) for x in str(acc)])

if __name__ == "__main__":
    print(euler_20(100))
