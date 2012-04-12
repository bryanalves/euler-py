#!/usr/bin/env python

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def euler_17(n):
    words = "".join((num_to_word(x) for x in range(1, n + 1)))
    return len(words)

def replace_dec(func):
    def wrapper(*args, **kwargs):
        retval = func(*args, **kwargs)
        return retval.replace('-', '').replace(' ', '')

    return wrapper

@replace_dec
def num_to_word(n):
    mapping = {
            0: "",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",

            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety",
    }

    thousands = n // 1000
    hundreds = n // 100
    rest = n - hundreds * 100

    hundreds -= thousands * 10

    retval = ""
    if thousands:
        retval += "%s thousand " % mapping[thousands]

    if hundreds:
        retval += "%s hundred " % mapping[hundreds]

    if rest == 0:
        return retval

    if rest in mapping:
        if thousands or hundreds:
            retval += "and %s" % mapping[rest]
        else:
            retval += mapping[rest]
    else:
        tens = (rest // 10) * 10
        ones = rest % 10
        if thousands or hundreds:
            retval += "and %s-%s" % (mapping[tens], mapping[ones])
        else:
            retval += "%s-%s" % (mapping[tens], mapping[ones])

    return retval

if __name__ == "__main__":
    print(euler_17(1000))
