#!/usr/bin/env python
from tqdm import tqdm
from math import ceil
import fractions

limit = 12000
count = 0
for i in tqdm(range(2, limit+1)):
    low = i/3+1
    high = (i+1)/2
    for j in range(low, high):
        gcd_val = fractions.gcd(i, j)
        if gcd_val == 1:
            count += 1

print count
