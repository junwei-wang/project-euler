#!/usr/bin/env python

res_list = list()

def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def permutation(arr, m, func):
    """A(n, m)"""
    arrlen = len(arr)
    if m == arrlen-4:
        func(arr)
        return
    for i in range(m, arrlen):
        swap(arr, m, i)
        permutation(arr, m+1, func)
        swap(arr, m, i)

def permuation(arr, func):
    permutation(arr, 0, func)

def is_pandigital(arr):
    a = arr[0]*10 + arr[1]
    b = arr[2]*100 + arr[3]*10 + arr[4]
    c = a*b
    if c < 10000 and set(str(a) + str(b) + str(c)) == set('123456789'):
        res_list.append(c)

    a = arr[0]
    b = arr[1]*1000 + arr[2]*100 + arr[3]*10 + arr[4]
    c = a*b
    if c< 10000 and set(str(a) + str(b) + str(c)) == set('123456789'):
        res_list.append(c)

input = map(int, '123456789')
permuation(input, is_pandigital)
print sum(set(map(int, res_list)))
