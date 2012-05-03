#!/usr/bin/env python

"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

import itertools
def euler_30(power):
    md_range = range(2, max_digits(power) + 1)
    combs_by_digit = (itertools.combinations_with_replacement(range(0, 10), x) for x in md_range)
    combs = itertools.chain(*combs_by_digit)

    matches = []
    for comb in combs:
        s = str(sum(x ** power for x in comb))
        comb = ''.join(str(y) for y in comb)
        match = (x for x in itertools.permutations(comb))
        match = list(filter(lambda x: ''.join(x) == s, match))
        if match:
            matches.append(''.join(match[0]))

    return sum(int(x) for x in matches)

def max_digits(power):
    digits = 1
    acc = 9 ** power

    while int("9" * digits) < acc:
        digits += 1
        acc += 9 ** power

    return digits

if __name__ == "__main__":
    print(euler_30(5))
