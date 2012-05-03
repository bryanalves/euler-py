#!/usr/bin/env python
"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

def euler_31(target):
    ways = [0] * (target + 1)
    ways[0] = 1
    values = [1, 2, 5, 10, 20, 50, 100, 200]

    for value in values:
        for i in range(value, target + 1):
            ways[i] += ways[i - value]

    return ways[target]

if __name__ == "__main__":
    print(euler_31(200))
