#!/usr/bin/env python

def is_permuted(n):
    s = sorted(str(n))

    if s == sorted(str(n*2)) == sorted(str(n*3)) == sorted(str(n*4)) == sorted(str(n*5)) == sorted(str(n*6)):
        return True
    return False


while True:
    time = 1
    for i in range(100000*time, 1000000*time/6):
        if is_permuted(i):
            print i
            exit()

    time += 1
