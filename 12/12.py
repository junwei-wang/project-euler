#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt, ceil

def get_fac_num(n):
    if n == 1:
        return 1

    sqr = int(ceil(sqrt(n)))
    sum = 2
    if sqr * sqr == n:
        sum += 1
    for i in range(2, sqr):
        if n % i == 0:

            sum += 2
    return sum

i = 10
while True:
    tri = i * (i+1) / 2
    fac_num = get_fac_num(tri)
    if fac_num > 500:
        print i, tri, fac_num
        break
    i += 1
