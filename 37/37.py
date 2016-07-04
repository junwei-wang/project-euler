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

    return sevie

number = 1000000
sevie = get_primes_under_n(number)
cnt = 0
sum = 0
for i in range(4, number/2):
    if not sevie[i]:
        continue
    p = 2*i + 1
    # >>>>>> right shift
    t = p / 10
    flag = True
    while flag:
        if t in [2, 3, 5, 7]:
            break
        if t & 1 == 0 or not sevie[t/2]:
            flag = False
        t /= 10

    if not flag:
        continue

    # <<<<<< left shift
    t = int(str(p)[1:])
    flag = True
    while flag:
        if t in [2, 3, 5, 7]:
            break
        if t & 1 == 0 or not sevie[t/2]:
            flag = False
            break
        t = int(str(t)[1:])
    if flag:
        cnt += 1
        sum += p
        if cnt >= 11:
            break

print sum
