#!/usr/bin/env python

from math import sqrt, ceil

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

def phi(n, primes):
    res = 1
    for p in primes:
        n_sqrt = int(sqrt(n))
        if p > n_sqrt:
            break
        if n % p:
            continue
        exp = 1
        n /= p
        while not n % p:
            exp += 1
            n /= p
        res *= (p-1) * (p ** (exp-1))
    if n > 1:
        res *= n-1
    return res
            

def run(limit=1000000):
    limit_sqrt = int(sqrt(limit))
    primes = generate_primes_under_n(limit_sqrt+1)

    sum = 0
    for i in range(2, limit+1):
        sum += phi(i, primes)
    print sum
run(limit=1000000)



