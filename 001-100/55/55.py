#!/usr/bin/env python

def is_palindromic(s):
    leng = len(s)
    half = leng / 2
    if s[:half] == s[leng-half:][::-1]:
        return True
    return False

def is_lychrel(n):
    s = str(n)
    cnt = 50
    while cnt > 0:
        s = str(int(s) + int(s[::-1]))
        if is_palindromic(s):
            return False
        cnt -= 1
    return True


sum = 0
for i in range(5, 10000):
    if is_lychrel(i):
        sum += 1

print sum
