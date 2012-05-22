#!/usr/bin/env python

import itertools
import lib

def euler_41():
    perms = (itertools.permutations(range(1, x), x - 1) for x in range(2, 11))
    perms = itertools.chain(*perms)
    perms = (int(''.join(map(str, x))) for x in perms)
    prime_perms = filter(lib.is_prime, perms)
    return max(prime_perms)

if __name__ == "__main__":
    print(euler_41())
