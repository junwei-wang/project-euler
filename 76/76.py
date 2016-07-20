#!/usr/bin/env python

limit = 100
matrix = list()
for i in range(limit+1):
    matrix.append([0] * limit)
matrix[0] = [0] + [1] * (limit-1)

# matrix[i][j] reprents that how to sum to i by using number <= j
for i in range(1, limit + 1):
    matrix[i][1] = 1
    for j in range(2, limit):
        cnt = 0
        ti = i
        while ti >= 0:
            cnt += matrix[ti][j-1]
            ti -= j
        matrix[i][j] = cnt

print matrix[limit][limit-1]
