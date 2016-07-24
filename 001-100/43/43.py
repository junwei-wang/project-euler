#!/usr/bin/env python

# d6 must be 5
d6 = 5

# d6d7d8 is divided by 11
l678 = list()
for i in range(500, 600):
    if i % 11 == 0:
        if len(set(str(i))) == 3:
            l678.append(i)
print l678

# d7d8d9 is divided by 13
l6789 = list()
for i in l678:
    t = i % 100
    t *= 10
    for j in range(0, 10):
        if (t + j) % 13 == 0:
            v = t + j + d6*1000
            if len(set(str(v))) == 4:
                l6789.append(v)
print l6789

# d8d9d10 is divided by 17
l678910 = list()
for i in l6789:
    t = i % 100
    t *= 10
    for j in range(0, 10):
        if (t + j) % 17 == 0:
            v = t + j + (i/100)*1000
            if len(set(str(v))) == 5:
                l678910.append(v)
print l678910

# d5d6d7 is divided by 10
l5678910 = list()
for i in l678910:
    t = i / 1000
    for j in range(0, 10):
        if (t + j*100) % 7 == 0:
            v = i + j*100000
            if len(set(str(v))) == 6:
                l5678910.append(v)

print l5678910

# full permutation
def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def permutation(arr, m, func):
    """A(n, m)"""
    arrlen = len(arr)
    if m == arrlen-1:
        func(arr)
        return
    for i in range(m, arrlen):
        swap(arr, m, i)
        permutation(arr, m+1, func)
        swap(arr, m, i)

def full_permuataion(arr, func):
    permutation(arr, 0, func)

sum = 0
def is_divisible(arr):
    global sum
    if arr[0] == '0':
        return
    if int(arr[3]) & 1 == 1:
        return

    t = ''.join(arr)
    for i in l5678910:
        if (int(arr[2]) + int(arr[3]) + i/100000) % 3 == 0:
            t2 = t + str(i)
            if len(set(t2)) == 10:
                sum += int(t2)


all_digit = set('0123456789')
for i in l5678910:
    rem_digit = list(all_digit - set(str(i)))
    full_permuataion(rem_digit, is_divisible)

print sum
