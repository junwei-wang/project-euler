#!/usr/bin/env python

vm = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

def is_straight(m):
    s = sorted(m.keys())
    return s[0] + 4 == s[-1]

def is_flush(m):
    v = m.values()
    return v[0] == v[1] == v[2] == v[3] == v[4]

def get_result(p):
    m = dict()
    for i in p:
        k = vm[i[0]]
        if k in m:
            m[k].append(i[1])
        else:
            m[k] = [i[1]]
    keys = m.keys()
    length = len(keys)

    if length == 5:
        flush = is_flush(m)
        straight = is_straight(m)
        if flush:
            if straight:
                print keys
                if max(keys) == 14:
                    return (9, m)
                return (8, m)
            return (5, m)
        if straight:
            return (4, m)
        return (0, m)
    elif length == 4:
        return (1, m)
    elif length == 3:
        if max(map(len, m.values())) == 3:
            return (3, m)
        return (2, m)
    else:
        if max(map(len, m.values())) == 4:
            return (7, m)
        return (6, m)
    return m

def compare(p1, p2):
    r1 = get_result(p1)
    r2 = get_result(p2)
    if r1[0] > r2[0]:
        return True
    elif r1[0] < r2[0]:
        return False
    else:
        if r1[0] == 0:
            return sorted(r1[1], reverse=True) > sorted(r2[1], reverse=True)
        elif r1[0] == 1:
            t1 = filter(lambda x: len(x[1])==2, r1[1].iteritems())[0][0]
            t2 = filter(lambda x: len(x[1])==2, r2[1].iteritems())[0][0]
            if t1 > t2:
                return True
            elif t1 < t2:
                return False
            else:
                r1[1].pop(t1)
                r2[1].pop(t1)
                return sorted(r1[1], reverse=True) > sorted(r2[1], reverse=True)
        else:
            print "something error!!!"


f = open('p054_poker.txt')
lines = f.read()
f.close()
lines = lines.split('\n')[:-1]


cnt = 0
for l in lines:
    t = l.split()
    if compare(t[:5], t[5:]):
       cnt += 1

print cnt
