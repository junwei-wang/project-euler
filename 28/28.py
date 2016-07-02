#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = 1001
half = (num+1) / 2

def squre_sum(n):
    return n*(n+1)*(2*n+1)/6

def sum(n):
    return n*(n+1)/2


print 4*(squre_sum(num+1) - 4*squre_sum(half)) - 6*(sum(num+1) - 2*sum(half)) + 6*half -3
