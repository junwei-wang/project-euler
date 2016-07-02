#!/usr/bin/env python

from math import log

length = 1000000 / 2
l = [0] * length
l[0] = 1 # 1
l[1] = 8 # 3
l[2] = 6 # 5
l2 = 2

for i in range(3, length):
    j = i
    chain = list()
    while j >= length or l[j] == 0:
        chain.append(j)
        # 3(2j+1)+1 = 6j + 4 is even
        t = 6*j + 4
        while t and t & 1 == 0:
            chain.append(0)
            t >>= 1
        j = (t-1)/2
    v = l[j] if t != 1 else 0

    for j in chain[::-1]:
        v += 1
        if j and j < length:
            l[j] = v

print 2*max(enumerate(l), key=lambda x: x[1])[0] + 1
