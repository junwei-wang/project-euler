#!/usr/bin/env python

from math import sqrt
from tqdm import tqdm
from itertools import count

def pentagon(n):
    return n * (3*n-1) / 2

def is_pentagonal(n):
    delta = 1+24*n
    sqr = int(sqrt(delta))
    if sqr*sqr == delta and sqr%6 == 5:
        return True
    return False

pentagon_list = [pentagon(i) for i in range(1, 3000)]

for i, n1 in tqdm(enumerate(pentagon_list)):
    for n2 in pentagon_list[:i]:
        if is_pentagonal(n1+n2) and is_pentagonal(n1-n2):
            print n1-n2
            exit()
