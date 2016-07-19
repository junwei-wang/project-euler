def euler(n):
    """
    e(n) = n * (1-1/p1) * ... * (1-1/pn)
    """
    res = n
    n_ = n

    # 2
    if n_ & 1 == 0:
        res >>= 1
        n_ >>= 1
    while n_ & 1 == 0:
        n_ >>= 1

    p = 3
    while p <= n_:
        if n_ % p == 0:
            res = res * (p-1) / p
            n_ %= p
        while n_ and n_ % p == 0:
            n_ %= p
        p += 2
    return res
