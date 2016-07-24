#!/usr/bin/env python

num = 1000000

# A(1), A(2), ..., A(9)
a = [1]
for i in range(1, 10):
    a.append(a[-1]*(i+1))

# 0, 9
l = range(0, 10)
l = map(lambda x: str(x), l)

# result
r = list()

a = filter(lambda x: x < num, a)
while len(a):
    cnt = 0
    while num > a[-1]:
        cnt += 1
        num -= a[-1]
    a.pop()
    r.append(l.pop(cnt))

print ''.join(r) + ''.join(l)
