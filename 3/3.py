#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = 600851475143
max_prime = 1
i = 3
while i <= num:
    while num % i == 0:
        max_prime = i
        num /= i
    i += 2
print max_prime
