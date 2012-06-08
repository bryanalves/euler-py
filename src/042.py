#!/usr/bin/env python

def euler_42():
    f = open('../data/words.txt')
    words = (word.replace('"', '') for word in f.readline().split(','))
    trianglewordsums = [sum([(ord(x) - 64) for x in word]) for word in words]
    triangles = list(triangle_gen(max(trianglewordsums)))
    return len(list(filter(lambda x: x in triangles, trianglewordsums)))


def triangle_gen(maximum):
    x = 1
    acc = 2
    while x < maximum:
        yield x
        x += acc
        acc += 1

if __name__ == "__main__":
    print(euler_42())
