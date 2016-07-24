#!/usr/bin/env python

from math import sqrt

limit = 1000000
a = 2
b = 5
for i in range(6, limit + 1):
    if i % 7 == 0:
        a2 = 3*i/7-1
    else:
        a2 = 3*i/7
    b2 = i
    if a*b2 < a2*b:
        a = a2
        b = b2

print a,b
while a & 1 == 0 and b & 1== 0:
    a >>= 1
    b >>= 1
sqrt_a = int(sqrt(a))

for i in range(3, sqrt_a, 2):
    while a % i == 0 and b % i == 0:
        a /= i
        b /= i
        print i, a, b
print a, b
