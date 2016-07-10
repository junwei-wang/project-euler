#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tqdm import tqdm


def factorial(n):
    if n == 0:
        return 1

    return reduce(lambda a, b: a*b, range(1, n+1))

fac = [factorial(i) for i in range(10)]

# the limit is less than 10^6 * 1 since
# 9999999 = 10^9-1 > 9! * 7
i = 1
while 10**i - 1 < fac[9] * i:
    i += 1
limit = fac[9] * i

# the real compute
total = 0
it = iter(range(10, limit))
for i in tqdm(it):
    si = str(i)
    x = sum(map(lambda i: fac[int(i)], si))
    if x == i:
        total += i

print total
