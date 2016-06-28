#!/usr/bin/env python
# -*- coding: utf-8 -*-
def fib(max):
    a = 1
    b = 1
    while a < max:
        if a & 1 == 0:
            yield a
        tmp = a + b
        a = b
        b = tmp

print sum(fib(4000000))
