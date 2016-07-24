#!/usr/bin/env python

# the number is at least 918273645
max = 918273645

# the bigger one is 9xxx18xxx, not the other form
# get the premutation of [2, 3, 4, 5, 6, 7]
def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t

def permutation(arr, m, func):
    """A(n, m)"""
    arrlen = len(arr)
    if m == arrlen-3:
        func(arr)
        return
    for i in range(m, arrlen):
        swap(arr, m, i)
        permutation(arr, m+1, func)
        swap(arr, m, i)

def permuation(arr, func):
    permutation(arr, 0, func)

max2 = int(str(max)[1:4])
l = '234567'
def func(arr):
    global max2
    t = arr[0]*100 + arr[1]*10 + arr[2]
    t2 = t*2
    if t < max2 or t2 > 1000:
        return

    if set(str(t)+str(t2)) == set(l):
        max2 = t

permuation(map(int, l), func)

print '9' + str(max2) + '18' + str(max2*2)
