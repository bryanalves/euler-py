#!/usr/bin/env python
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def euler_10(prime_max):
    return sum(prime_sieve(prime_max))

def prime_sieve(prime_max):
    numlist = list(range(prime_max + 1))

    for i in range(2, int(prime_max ** 0.5) + 1):
        if numlist[i]:
            numlist[2*i::i] = [False] * (prime_max // i - 1)

    return (i for i in numlist[2:] if i)

if __name__ == "__main__":
    print(euler_10(2000000))
