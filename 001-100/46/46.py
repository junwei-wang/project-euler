#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt, ceil

def get_primes_under_n(num):
    length = int(ceil(num/2.0))
    sevie = [True] * length # 1, 3, 5, 7, ..., n-1
    sevie[0] = False

    # a number has at most one factor than its squre
    sqr = int(ceil(sqrt(num)))
    sqr_idx = (sqr+1)/2
    for i in range(1, sqr_idx):
        if sevie[i]:
            start = 3*i + 1
            step = 2*i + 1
            for j in range(start, length, step):
                sevie[j] = False

    primes = [2*k+1 for k, v in enumerate(sevie) if v]
    primes = [2] + primes

    return primes

num = 10000
primes = get_primes_under_n(num)
squres = [i*i*2 for i in range(int(sqrt(num))+1)]

can = [False] * (num/2)
can[0] = [True]  # 1
can[1] = [True]  # 3
can[2] = [True]  # 5
can[3] = [True]  # 7
for i, p in enumerate(primes):
    if not can[i]:
        print 2*i+1
        break
    for s in squres:
        sum = p + s
        if sum < num:
            can[sum/2] = True

for n in range(i+1, len(can)):
    if not can[n]:
        print 2*n+1
        break
