#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt, ceil

num = 2000000
sevie = [True] * num # 0, 1, 2, 3, ..., 1999999

sevie[0] = False
sevie[1] = False
for i in range(3, num):
    if i & 1 == 0:
        sevie[i] = False

# a number has at most one factor than its squre
sqr = int(ceil(sqrt(num)))
for i in range(3, sqr):
    if sevie[i]:
        # start from the prime multiple: 3i with step: 2i
        for j in range(3*i, num, 2*i):
            sevie[j] = False

sum = 0
for idx, val in enumerate(sevie):
    if val:
        sum += idx

print sum
