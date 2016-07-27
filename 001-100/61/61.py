#!/usr/bin/env python

def get_map(func, start, end):
    map_ = dict()
    for i in range(start, end+1):
        p = func(i)
        div_, mod_ = divmod(p, 100)
        if mod_ < 10:
            continue
        if mod_ in map_:
            map_[mod_].append(div_)
        else:
            map_[mod_] = [div_]
    return map_

maps = [0]*6
maps[5] = get_map(lambda x: x*(x+1)/2, 45, 140)
maps[4] = get_map(lambda x: x*x, 31, 99)
maps[3] = get_map(lambda x: x*(3*x-1)/2, 26, 81)
maps[2] = get_map(lambda x: x*(2*x-1), 23, 70)
maps[1] = get_map(lambda x: x*(5*x-3)/2, 21, 63)
maps[0] = get_map(lambda x: x*(3*x-2), 19, 58)

# permuation of [1,2,3,4,5]
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

def full_permutation(arr, func):
    permutation(arr, 0, func)


def check(arr):

    for k0 in maps[0].keys():
        v0 = maps[0][k0]
        for k1 in v0:
            if k1 not in maps[arr[0]]:
                continue
            v1 = maps[arr[0]][k1]
            for k2 in v1:
                if k2 not in maps[arr[1]]:
                    continue
                v2 = maps[arr[1]][k2]
                for k3 in v2:
                    if k3 not in maps[arr[2]]:
                        continue
                    v3 = maps[arr[2]][k3]
                    for k4 in v3:
                        if k4 not in maps[arr[3]]:
                            continue
                        v4 = maps[arr[3]][k4]
                        for k5 in v4:
                            if k5 not in maps[arr[4]]:
                                continue
                            v5 = maps[arr[4]][k5]
                            if k0 in v5:
                                print (k1+k2+k3+k4+k5+k0)*101
                                exit()

full_permutation([1,2,3,4,5], check)
