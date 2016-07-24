#!/usr/bin/env python

from math import sqrt, floor

length = 10000
l = [0] * length

def get_divisor_sum(n):
    dsum = 1
    isqr = int(floor(sqrt(n)))
    if isqr * isqr == n:
        dsum -= isqr
    for j in range(2, isqr+1):
        if n % j == 0:
            dsum += (j + n/j)
    return dsum

sum = 0
for i in range(3, length):
    if l[i] < 0:
        continue

    dsum = get_divisor_sum(i)
    if i == dsum:
        continue
    ddsum = get_divisor_sum(dsum)

    if ddsum == i:
        if dsum < length:
            l[dsum] = -1
        sum += i + dsum

print sum
