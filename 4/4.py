#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_palindromic(num):
    num = str(num)
    for i in range(len(num)/2):
        if num[i] != num[-i-1]:
            return False
    return True

max = 0
# only search 11's multiple, since 111111=143*777
# p(x) = xyzzyx (6 digits) = 100000x + 10000y + 1000z + 100z + 10y + x
#      = 11(9091x + 910y + 100z)
#
# search backforward
for i in range(990, 100, -11):
    # stop search if the digit is small
    if i * 999 <= max:
        break
    for j in range(999, 100, -1):
        prod = i * j
        if prod < max:
            continue
        if is_palindromic(prod):
            max = prod

print max
