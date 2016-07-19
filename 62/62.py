#!/usr/bin/env python

d = dict()

for i in range(10,100000):
    s = str(i**3)
    s = ''.join(sorted(s))
    if s in d:
        d[s].append(i)
        if len(d[s])>=5:
            print d[s][0]**3
            break
    else:
        d[s]=[i]
