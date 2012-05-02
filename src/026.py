#!/usr/bin/env python

import lib

def euler_26(n):
    return max((num_repeating(x), i + 1) for i,x in enumerate(range(1, n+1)) if lib.is_prime(x))[1]

def num_repeating(n):
    pw = 1

    while (10 ** pw) % n != 1:
        if pw > n: return 0
        pw += 1

    return pw

if __name__ == "__main__":
    print(euler_26(1000))
