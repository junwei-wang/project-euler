#!/usr/bin/env python
# -*- coding: utf-8 -*-

total = 200
l = [1, 2, 5, 10, 20, 50, 100, 200]

# coins[n][m] represents how many way to get n by m kinds of coins
coins = [[0 for col in range(len(l)-1)] for row in range(total+1)]
for i in coins:
    i[0] = 1
coins[0] = [1] * len(l)
coins[1] = [1] * len(l)

for i in range(2, total+1):
    for j in range(1, len(l)-1):
        num = 0
        t = i
        while t >= 0:
            num += coins[t][j-1]
            t -= l[j]
        coins[i][j] = num

print coins[total][len(l)-2] + 1
