#!/usr/bin/env python

import itertools
import lib

def penta_gen():
    n = 1
    while True:
        yield (n, n * ((3 * n) - 1) / 2)
        n += 1

def penta_gen_decrementing(n):
    while n > 0:
        yield n * (3 * n - 1) / 2
        n -= 1

def penta_filter(f):
    return lib.is_penta(f[0] + f[1]) and lib.is_penta(f[0] - f[1])

def euler_44():
    pentas = penta_gen()
    while True:
        n, penta = next(pentas)
        pentas2 = penta_gen_decrementing(n)
        pairs = ((penta, x) for x in pentas2)
        match = list(itertools.islice(filter(penta_filter, pairs), 1))
        if len(match) > 0:
            match = match[0]
            return match[0] - match[1]

if __name__ == "__main__":
    print(euler_44())
