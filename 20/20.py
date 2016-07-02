#!/usr/bin/env python

from math import log

v = reduce(lambda x, y: x*y, [i for i in range(1, 101)])
print sum(map(int, str(v)))
