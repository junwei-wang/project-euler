#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import ceil, sqrt

num = 600851475143
max_prime = 1
sqr = int(ceil(sqrt(num)))
i = 3
while i <= num and i < sqr:
    while num % i == 0:
        max_prime = i
        num /= i
    i += 2
if num >= sqr:
    max_prime = num
print max_prime
