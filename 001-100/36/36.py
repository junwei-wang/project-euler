#!/usr/bin/env python
# -*- coding: utf-8 -*-

sum = 0
for i in range(1, 1000):
    stri = str(i)
    if int(stri[0]) & 1 == 0:
        continue
    leni = len(stri)
    revi = stri[::-1]

    t = int(stri+stri[::-1])
    s = '{0:b}'.format(t)
    if s == s[::-1]:
        sum += t

    t = int(stri + stri[:leni-1][::-1])
    s = '{0:b}'.format(t)
    if s == s[::-1]:
        sum += t

print sum
