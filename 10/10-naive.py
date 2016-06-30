#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt, ceil

primes = [2, 3]

def is_prime(n):
    sqr = ceil(sqrt(n))
    for p in primes:
        # a number can only have one factor bigger than its squre
        # hence, a prime number has no factor lower than its squre
        if p > sqr:
            return True
        if n % p == 0:
            return False

    return True

# any primer bigger than 3 can be written in 6k+1 or 6k-1
def find_primes_below_n(n):
    global primes
    if n == 2:
        primes = [4]
        return
    if n == 4:
        primes = [5]
        return
    num = 0
    while True:
        num += 6
        if num - 1 >= n:
            break
        if is_prime(num-1):
            primes.append(num-1)
        if num + 1 >= n:
            break
        if is_prime(num+1):
            primes.append(num+1)

find_primes_below_n(2000000)
print sum(primes)
