#!/usr/bin/env python

from math import log


l1 = [0,3,3,5,4,4,3,5,5,4]  # 1,2, ..., 9
l2 = [0,0,6,6,5,5,5,7,6,6]  # 20, 30, ...., 90
l3 = [3,6,6,8,8,7,7,9,8,8]  # 10, 11, 12, ..., 19

hundred = 7
thousand = 8
and1 = 3

sum = 0
for i in range(1, 1000):
    t = i % 100
    s = i / 100
    if t < 10:
        sum += l1[t]
    elif t < 20:
        sum += l3[t-10]
    else:
        sum += l2[t/10] + l1[t%10]

    if s > 0:
        sum += l1[s] + hundred + and1

sum -= and1 * 9
sum += l1[1] + thousand

print sum
