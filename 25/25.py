#!/usr/bin/env python

a = 1
b = 1
idx = 2
while (len(str(b)) < 1000):
    t = a + b
    a = b
    b = t
    idx += 1

print idx
