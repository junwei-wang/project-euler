#!/usr/bin/env python
from math import sqrt,ceil
from tqdm import tqdm

limit = 10 ** 8
limit_sqrt = int(sqrt(limit))

# odd is not ok
# 4k is not ok
# only 4k+2 is ok

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

    return sevie

sevie = generate_primes_under_n(limit)

def is_prime(n):
    if n == 2:
        return True
    if n & 1 == 0:
        return False
    if n <= limit:
        return sevie[(n-1)/2]
    raise Exception('cannot be here')

sum = 1+2
for i in tqdm(range(1, limit/4)):
    n = i*4 + 2
    n_sqrt = int(sqrt(n))
    if n_sqrt ** 2 == n:
        continue

    flag = True
    for j in range(1, n_sqrt+1):
        if n % j == 0:
            tmp = j + (n / j)
            if not is_prime(tmp):
                flag = False
                break
    if flag:
        sum += n
print sum
