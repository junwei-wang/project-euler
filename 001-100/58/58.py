#!/usr/bin/env python

from math import ceil, sqrt
from tqdm import tqdm

def generate_primes_under_n(num):
    length = int(ceil(num/2.0))
    sevie = [True] * length # 1, 3, 5, 7, ..., n-1
    sevie[0] = False

    # a number has at most one factor than its squre
    sqr = int(ceil(sqrt(num)))
    sqr_idx = (sqr+1)/2
    for i in range(1, sqr_idx):
        if sevie[i]:
            start = 3*i + 1
            step = 2*i + 1
            for j in range(start, length, step):
                sevie[j] = False

    primes = [2*k+1 for k, v in enumerate(sevie) if v]
    primes = [2] + primes

    return primes


limit = 40000
primes = generate_primes_under_n(limit)

def is_prime(n):
    # for numbers under limit**2
    sqr = sqrt(n)
    for p in primes:
        if n % p == 0:
            return False
        if p > sqr:
            return True

    return True

primes_number = 8
for i in tqdm(range(9, limit, 2)):
    total_number = (i/2) * 4 + 1
    if is_prime(i*i-i+1):
        primes_number += 1
    if is_prime(i*i-2*i+2):
        primes_number += 1
    if is_prime(i*i-3*i+3):
        primes_number += 1

    if (primes_number * 1.0 / total_number) < 0.1:
        print i
        break
