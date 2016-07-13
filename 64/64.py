#!/usr/bin/env python

from math import sqrt


def get_continued_fractions(n):
    sqr = sqrt(n)
    # a0 (a, b/(sqrt(c)-d))
    (a, b, c) = (int(sqr), 1, n)
    d = a

    # a1
    x = (c-d*d)/b
    t = int(b/(sqrt(c) - d))
    (a, b, c, d) = (t, x, c, t*x-d)

    # initial
    (a0, b0, c0, d0) = (a, b, c, d)

    l = [a]
    while True:
        x = (c-d*d)/b
        t = int(b/(sqrt(c) - d))
        (a, b, c, d) = (t, x, c, t*x-d)
        if a == a0 and b == b0 and c == c0 and d == d0:
            break
        else:
            l.append(a)
    return (int(sqr), l)


limit = 10000
count = 0
for i in range(2, limit + 1):
    sqr_t = int(sqrt(i))
    if sqr_t ** 2 == i:
        continue
    t = get_continued_fractions(i)
    if len(t[1]) & 1 == 1:
        count += 1
print count
