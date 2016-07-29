#!/usr/bin/env python
from math import ceil, sqrt

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

def run(limit=50000000):
    a = int(limit**0.5)
    b = int(limit**(1/3.0))
    c = int(limit**0.25)
    primes = generate_primes_under_n(a+1)
    res = set()

    for p0 in primes:
        if p0 > c:
            break
        n0 = p0**4

        for p1 in primes:
            if p1 > b:
                break
            n1 = p1 ** 3
            if n0 + n1 > limit:
                break

            for p2 in primes:
                n2 = p2**2
                s = n0+n1+n2
                if s > limit:
                    break
                else:
                    res.add(s)
    print len(res)

run()
