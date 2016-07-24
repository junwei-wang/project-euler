#!/usr/bin/env python

d1 = 1
d10 = 1

def get_d_n(n):
    if n < 10:
        return n
    if n < 190:  # 9 + 2 * 90 + 1:
        t = n - 10
        s = 10 + (t>>1)
        return str(s)[t&1]
    if n < 2890: # 9 + 2*90 + 3*900 + 1
        t = n - 190
        s = 100 + t / 3
        return str(s)[t%3]
    if n < 38890: # 9 + 2*90 + 3*900 + 4*9000
        t = n - 2890
        s = 1000 + (t>>2)
        return str(s)[t&0b11]
    if n < 488890: # 38890 + 5*90000
        t = n - 38890
        s = 10000 + (t/5)
        return str(s)[t%5]
    if n < 5888890: # 38890 + 5*90000 + 6*900000
        t = n - 488890
        s = 100000 + (t/6)
        return str(s)[t%6]

prod = 1
for i in range(1, 7):
    prod *= int(get_d_n(10**i))
print prod
