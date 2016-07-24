#!/usr/bin/env python

from math import sqrt

def is_full_sqr(n):
    sqr = int(sqrt(n))
    if sqr * sqr == n:
        return sqr
    return False

# a + b > c
# a < b < c < 500
limit = 500
sum_cnt = dict()
for b in range(1, limit):
    for a in range(1, b):
        s = a*a + b*b
        sqr = is_full_sqr(s)
        if sqr:
            sum = a + b + sqr
            if sum <= 1000:
                if sum in sum_cnt:
                    sum_cnt[sum] += 1
                else:
                    sum_cnt[sum] = 1

print max(sum_cnt.iteritems(), key=lambda x: x[1])[0]
