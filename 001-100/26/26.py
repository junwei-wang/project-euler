#!/usr/bin/env python

from tqdm import tqdm

def get_cycle_len(n):
    v = 10
    d = list()
    r = list()
    collison = [False] * (10*n)
    while True:
        # print v, n
        if v < n:
            d.append(0)
            r.append(v)
            if collison[v]:
                break
            else:
                collison[v] = True
        else:
            t = v/n
            v %= n
            d.append(t)
            r.append(v)
            if collison[t*n + v]:
                break
            else:
                collison[t*n + v] = True

        if v == 0:
            return 0
        v *= 10

    for k1, v1 in enumerate(d):
        for k2, v2 in enumerate(d[k1+1:]):
            if v1 == v2 and r[k1] == r[k1+k2+1]:
                # print d, r
                return k2 + 1



lens = [get_cycle_len(i) for i in tqdm(range(7, 1000))]
print lens.index(max(lens)) + 7
