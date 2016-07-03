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

def is_arithmetic(a, b):
    return set(str(a)) == set(str(b))

num = 10000
primes = get_primes_under_n(num)
primes = filter(lambda x: x>1000 and x not in [1487, 4817, 8147], primes)

for i, p1 in enumerate(primes):
    for j, p2 in enumerate(primes[i+1:]):
        if not is_arithmetic(p1, p2):
            continue
        p3 = 2*p2 -p1
        if not is_arithmetic(p1, p3):
            continue

        if p3 in primes[j+1:]:
            print str(p1) + str(p2) + str(p3)
            exit()
