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

num = 1000000
primes_list = get_primes_under_n(num)


max = 21
val = 953
prime_cnt = len(primes_list)
for i, prime in enumerate(primes_list):
    # break if the are less than max primes
    if i + max > prime_cnt:
        break

    s = sum(primes_list[i:i+max])
    cnt = max

    # break if s bigger than num
    if s > num:
        break

    # brute force
    for j in primes_list[i+max:]:
        s += j
        cnt += 1
        if s in primes_list[i+cnt:]:
            max = cnt
            val = s
        # break if s is too big
        if s > num:
            break

print val
