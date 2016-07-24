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
cnt = 13
start = 100 / 2
not_set = set(['0', '2', '4', '6', '8', '5'])
for i in range(start, number/2):
    if not sevie[i]:
        continue

    p = 2*i + 1
    sp = str(p)
    if not_set & set(sp):
        continue
    lenp = len(sp)

    flag = True
    p2 = p
    for i in range(1, lenp):
        p2 = p2/10 + (p2%10)*(10**(lenp-1))
        if not sevie[p2/2]:
            flag = False
            break

    if flag:
        cnt += 1

print cnt
