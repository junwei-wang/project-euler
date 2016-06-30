#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Get first n-th primes numbers

from math import sqrt, ceil

def is_prime(num, prime_list):
    sqr = ceil(sqrt(num))
    for p in prime_list:
        if p > sqr:
            return True
        if num % p == 0:
            return False
    return True

def get_first_n_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    i = 18
    while len(primes) < n:
        print i
        i += 6
        if is_prime(i-1, primes):
            primes.append(i-1)
            print primes
        if is_prime(i+1, primes):
            primes.append(i+1)
    return primes
