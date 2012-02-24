#!/usr/bin/env python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def euler_3(composite):
    START_FACTOR = 2
    factor = START_FACTOR

    while composite > START_FACTOR:
        if composite % factor == 0:
            composite /= factor
        else:
            factor += 1

    return factor

if __name__ == "__main__":
    #print(euler_3(13195))
    print(euler_3(600851475143))
