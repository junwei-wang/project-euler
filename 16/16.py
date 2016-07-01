#!/usr/bin/env python

from math import log

x = 2
y = 1000

# get sum of exp of 2 = y
t = y
exp = 0
l = list()
while y > 0:
    if y & 1:
        l.append(exp)
    exp += 1
    y >>= 1

# get mult
mult = x         # x ^ 1 = x ^ (2^0)
cur_exp = 0
res = 1
for exp in l:
    while cur_exp < exp:
        mult **= 2
        cur_exp += 1
    res *= mult

print sum(map(int, str(res)))
