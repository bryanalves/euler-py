#!/usr/bin/env python
"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

def euler_39(m):
    #a^2 + b^2 = c^2 mean a + b + c is always even
    return max((count_solutions(x), x) for x in range(2, m, 2))[1]

def count_solutions(x):
    #a^2 + b^2 = c ^ 
    #a + b + c = x
    #c = (x - a - b)
    #a^2 + b^2 = (x - a - b)
    #a ^2 + b ^2 = x^2 + a^2 + b^2 - 2*x*a - 2*x*b + 2*a*b
    #b = x * (x - 2 * a) / (2 * (x -a))
    retval = 0
    for a in range(1, x // 4):
        b = x * (x - 2 * a) / (2 * (x -a))
        if b == int(b) and (a ** 2 + b ** 2) ** 0.5 == (x - a - b):
            retval += 1
    #don't care about a,b transpositions, just return the duplicates, it won't change the ordering of results
    return retval

if __name__ == "__main__":
    print(euler_39(1000))
