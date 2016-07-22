#!/usr/bin/env python
from tqdm import tqdm
from math import ceil
import fractions

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    else:
        return gcd(a%b, b)

limit = 12000
fraction = set()
for i in tqdm(range(2, limit+1)):
    low = i/3+1
    high = (i+1)/2
    for j in range(low, high):
        gcd_val = fractions.gcd(i, j)
        fraction.add((i/gcd_val, j/gcd_val))

print len(fraction)
