#!/usr/bin/env python

from tqdm import tqdm

def square_digit_sum(n):
    return reduce(lambda x, y: x+y, map(lambda x: int(x)**2, str(n)))

table_size = (9**2) * 7 + 1
table = [0] * (table_size)

for i in tqdm(range(1, table_size)):
    t = i
    while t != 1 and t != 89:
        t = square_digit_sum(t)
    table[i] = t

count = len([i for i in table if table[i] == 89])


for i in tqdm(range(table_size, 10000000)):
    if table[square_digit_sum(i)] == 89:
        count += 1

print count
