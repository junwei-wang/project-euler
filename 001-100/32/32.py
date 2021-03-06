#!/usr/bin/env python

res_list = list()

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

def permuation(arr, func):
    permutation(arr, 0, func)


def is_pandigital(arr):
    a = ''.join(arr[:2])
    b = ''.join(arr[2:5])
    c = ''.join(arr[5:])
    if int(a) * int(b) == int(c):
        res_list.append(c)
    a = arr[0]
    b = ''.join(arr[1:5])
    c = ''.join(arr[5:])
    if int(a) * int(b) == int(c):
        res_list.append(c)


input = list('123456789')
res_set = list()
permuation(input, is_pandigital)
print sum(set(map(int, res_list)))
