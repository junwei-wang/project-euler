#!/usr/bin/env python

from math import sqrt


limit = 10**6
last6 = []
for i in range(25, limit):
    sqr = i * i
    if sqr % 10 == 9 and (sqr/100)%10 == 8 and (sqr/10000)%10 == 7:
        last6.append(i)

min_ = int(sqrt(10203040506070809))
max_ = int(sqrt(19293949596979899))

for i in range(min_/limit, max_/limit+1):
    start = i * limit
    for l in last6:
        v = l + start
        sqr = (v*v)/limit
        n = 6
        while n >= 1 and sqr % 10 == n:
            sqr /= 100
            n -= 1
        if n <= 0:
            print str(v) + '0'
            exit()
