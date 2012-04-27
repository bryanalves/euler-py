#!/usr/bin/env python
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def euler_22():
    f = open('../data/names.txt')
    names = sorted(f.readlines()[0].replace('"', '').split(','))
    return sum([sum_name(name) * (position + 1) for position, name in enumerate(names)])

def sum_name(name):
    return sum([ord(x) - 64 for x in name])

if __name__ == "__main__":
    print(euler_22())
