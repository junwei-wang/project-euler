#!/usr/bin/env python

def f(n):
    prod = 1
    while n>=1:
        prod *=n
        n -= 1
        return prod

def c(n, r):
    return f(n)/(f(r)*f(n-r))


limit = 1000000
cnt = 0
for i in range(23, 101):
    last = i
    half = (i+1)/2
    for j in range(2, half):
        last = last * (i-j+1) / j
        if last > limit:
            cnt += i - 2*j + 1
            break

print cnt
