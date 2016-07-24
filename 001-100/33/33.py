#!/usr/bin/env python

f = lambda i, j, ti, tj: i*tj == j*ti
numerator = 1
denominator = 1
for i in range(10, 100):
    if i % 10 == 0:
        continue
    for j in range(i+1, 100):
        if j % 10 == 0:
            continue
        i0 = i % 10
        i1 = i / 10
        j0 = j % 10
        j1 = j / 10
        if i0 == j0:
            if f(i, j, i1, j1):
                numerator *= i1
                denominator *= j1
        elif i0 == j1:
            if f(i, j, i1, j0):
                numerator *= i1
                denominator *= j0
        elif i1 == j0:
            if f(i, j, i0, j1):
                numerator *= i0
                denominator *= j1
        elif i1 == j1:
            if f(i, j, i0, j0):
                numerator *= i0
                denominator *= j0

print numerator, denominator
