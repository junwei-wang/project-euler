#!/usr/bin/env python

from math import log

f = open('p099_base_exp.txt')
lines = f.read().strip().split()
f.close()

line = 0
max_ = 0
max_line = 0
for l in lines:
    line += 1
    l = l.split(',')
    a = int(l[0])
    b = int(l[1])
    tmp = b * log(a)
    if tmp > max_:
        max_ = tmp
        max_line = line

print max_line
