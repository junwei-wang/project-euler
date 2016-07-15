#!/usr/bin/env python

def get_nth(n):
    n -= 1
    if n == 0:
        return 2

    t = n
    m = (t-1) % 3
    a = (t/3+1)*2 if m == 1 else 1
    (b, c) = (0, 1)

    while t > 0:
        t -= 1
        m = (t-1) % 3
        (b, c) = (c, a*c+b)
        a = (t/3+1)*2 if m == 1 else 1
    return 2*c+b, c


print reduce(lambda x,y: x+y, map(int, str(get_nth(100)[0])))
