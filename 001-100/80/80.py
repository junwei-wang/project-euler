#!/usr/bin/env python

from decimal import Decimal, getcontext

getcontext().prec = 105

total = 0
for i in range(2,101):
      sqrt = Decimal(i).sqrt()
      if int(sqrt) ** 2 == i:
          continue
      total += int(sqrt) + sum(map(int, str(sqrt)[2:101]))
print total
