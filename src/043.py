#!/usr/bin/env python

import itertools

def divis_filter(inp):
    for x in [(2, 2),
            (3, 3),
            (4, 5),
            (5, 7),
            (6, 11),
            (7, 13),
            (8, 17),
            ]:
        x1, divis = x
        r = inp[x1-1:x1+2]
        if int("".join(map(str, r))) % divis != 0:
            return False

    return True



def euler_43():
    pandigitals = itertools.permutations(range(10))
    filtered = filter(divis_filter, pandigitals)

    x = (int("".join(map(str, x))) for x in filtered)
    return sum(x)

if __name__ == "__main__":
    print(euler_43())
