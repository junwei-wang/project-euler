#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t


def permutation(arr, m, func):
    """A(n, m)"""
    arrlen = len(arr)
    if m == arrlen-1:
        func(arr)
        return

    for i in range(m, arrlen):
        swap(arr, m, i)
        permutation(arr, m+1, func)
        swap(arr, m, i)

def permuation(arr, func):
    permutation(arr, 0, func)


# num = 987654321 is not prime (has factor 3)
# num = 87654321 is not prime (has factor 3)

num = 7654321
primes = generate_primes_under_n(int(ceil(sqrt(num))))
max = 2143

def is_prime(arr):
    global max
    arr = map(str, arr)
    num = int(''.join(arr))
    for p in primes:
        if num % p == 0:
            return False
    if num > max:
        max = num

permuation(map(int, str(num)), is_prime)
print max
