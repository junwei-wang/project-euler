#!/usr/bin/env python

total = 99 * 99

for i in [2, 3, 5, 6, 7, 10]:
    v = i
    cnt = 1
    repeated = 0
    all = range(2, 101)
    while v*i <= 100:
        v *= i
        cnt += 1
        all += range(2*cnt, 101*cnt, cnt)

    total -= 99 * cnt - len(set(all))

print total
