#!/usr/bin/env python

from tqdm import tqdm

factorial = [1] * 10
for i in range(2, 10):
    factorial[i] = factorial[i-1] * i
print factorial
#exit()
limit = 10 ** 6
limit = 10 ** 6
chain_len = [0] * limit
chain_len[1] = 1
chain_len[145] = 1
chain_len[169] = 3
chain_len[871] = 2
chain_len[872] = 2
chain_len[1454] = 3
chain_len[45361] = 2
chain_len[45362] = 2
chain_len[363601] = 3


def get_next(num):
    return reduce(lambda x, y: x+y, map(lambda x: factorial[int(x)], str(num)))

count = 0
for i in tqdm(range(2, limit)):
    if chain_len[i]:
        continue

    chain = list()
    t = i
    while t not in chain:
        if t<limit and chain_len[t]:
            break
        chain.append(t)
        t = get_next(t)
    chain_len[i] = len(chain) + chain_len[t]
    if chain_len[i] >= 60:
        count += 1
    else:
        for idx, v in enumerate(chain):
            if v > i and v < limit:
                chain_len[v] = chain_len[i] - idx

print count
