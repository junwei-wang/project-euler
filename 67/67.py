#!/usr/bin/env python

from math import log

# load data
f = open('p067_triangle.txt')
num = f.read()
f.close()
num = map(int, num.split())
n = 100

# cal
fun_max = lambda a, b: a if a>b else b
for i in range(1, n):
    idx = i * (i+1) / 2
    num[idx] += num[idx-i]
    num[idx+i] += num[idx-1]
    for j in range(1, i):
        idx2 = idx+j
        num[idx2] += fun_max(num[idx2-i], num[idx2-i-1])

print max(num[-n:])
