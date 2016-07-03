#!/usr/bin/env python

max = 1000
mod = 10000000000

sum = 0
for i in range(1, max+1):
    sum += pow(i, i, mod)

print str(sum)[-10:]
