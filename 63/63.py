#!/usr/bin/env python

i = 0
cnt = 0
start = 1
while True:
    i += 1
    first = True
    if len(str(start ** i)) < i and start >= 9:
        break
    for j in range(start,10):
        if len(str(j**i)) == i:
            if first:
                start=j
                first=False
                cnt += 1

print cnt
