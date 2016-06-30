#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt, ceil

num = 2000000
length = num / 2
sevie = [True] * length # 1, 3, 5, 7, ..., 1999999

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

sum = 2
for idx, val in enumerate(sevie):
    if val:
        sum += 2*idx + 1

print sum
