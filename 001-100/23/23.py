#!/usr/bin/env python

from math import sqrt, floor

length = 28123
l = [False] * length # 0, 1, 2, ..., 28123-1
l[12] = True

def get_divisor_sum(n):
    dsum = 1
    isqr = int(floor(sqrt(n)))
    if isqr * isqr == n:
        dsum -= isqr
    for j in range(2, isqr+1):
        if n % j == 0:
            dsum += (j + n/j)
    return dsum

for i in range(14, length):
    dsum = get_divisor_sum(i)
    if dsum > i:
        l[i] = True

sum = (23 * 24)/2
for i in range(25, length):
    flag = True
    for j in range(1, i/2+1):
        if l[j] and l[i-j]:
            flag = False
            break
    if flag:
        print i
        sum += i

print sum
