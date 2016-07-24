#!/usr/bin/env python

from math import sqrt

# a rectangular grid measuring n by m contains
# m*n*(m+1)*(n+1)/4 rectangles

limit = 2 * (10**6) * 4.0
limit_sqrt = int(sqrt(limit))

min_ = limit
m_ = 0
n_ = 0

for n in range(1, limit_sqrt):
    m = int(sqrt(limit/(n*(n+1))))
    sub = n*m*(m+1)*(n+1) - limit
    if sub < 0:
        sub1 = n*(m+1)*(n+1)*(m+2) - limit
        if abs(sub1) < abs(sub):
            sub = sub1
            m += 1
    sub = abs(sub)
    if sub < min_:
        min_ = sub
        m_ = m
        n_ = n

print m_*n_
