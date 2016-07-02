#!/usr/bin/env python

from math import log

length = 1000000
l = [0] * length
l[0] = 1 # 1
l[1] = 2 # 2
l[2] = 8 # 3
l[3] = 3 # 4
l[4] = 6 # 5

for i in range(5, length):
    if l[i]:
        d = 2*i+1
        if d < length and l[d] == 0:
            l[d] = l[i]+1
        else:
            pass
    else:
        # i+1 must be odd
        j = i
        chain = list()
        while j >= length or l[j] == 0:
            chain.append(j)
            if (j+1) & 1 == 1:
                j = 3*(j+1)+1 - 1
            else:
                j = (j+1)/2 - 1
        v = l[j]
        for j in chain[::-1]:
            v += 1
            if j < length:
                l[j] = v

print max(enumerate(l), key=lambda x: x[1])[0] + 1
