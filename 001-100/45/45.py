#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt, ceil

# H(n) = 2T(n-1) + n^2
# H(n) = 2P(n) - n^2

a = set([i*(i+1)/2 for i in range(1,100000)])
b = set([i*(3*i-1)/2 for i in range(1,100000)])
c = set([i*(2*i-1) for i in range(1,100000)])

print a & b & c
