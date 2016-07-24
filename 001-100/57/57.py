#!/usr/bin/env python

a = 3
b = 2
count = 0
for i in range(1, 1000):
    a += b
    b += a
    t = a
    a = b
    b = t
    if len(str(a)) > len(str(b)):
        count += 1

print count
