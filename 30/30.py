#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tqdm import tqdm

pow = [x**5 for x in range(10)]
last_digit_pow = map(lambda x: x%10, pow)

# the limit is less than 10^6 * 1 since
# 999999 = 10^6-1 > 9^5 * 6
i = 1
while 10**i - 1 < pow[9] * i:
    i += 1
limit = pow[9] * i
print 'limit =', limit

# the real compute
total = 0
for i in tqdm(range(10, limit)):
    x = sum(map(lambda i: pow[int(i)], str(i)))
    if x == i:
        total += i

print total
