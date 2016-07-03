#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt, ceil

def get_primes_under_n(num):
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

def has_n_factor(num, n, primes):
    sqr = sqrt(num)
    for p in primes:
        if p > sqr or p > num:
            break

        flag = False
        while num % p == 0:
            num /= p
            flag = True
        if flag:
            n -= 1

        # return False if num has more fator
        if n <= 0 and num > 1:
            return False

    return n==0 or (n==1 and num != 1) # if n==1, num must has a prime factor than its squre

num = 100000
primes = get_primes_under_n(num)
factors = 4

cur = 210  # 210: 2 * 3 * 5 * 7
while True:
    cnt = 0
    while (has_n_factor(cur, factors, primes)):
        cnt += 1
        if cnt == factors:
            print cur-3
            exit()
        cur += 1

    cur += 1
