#!/usr/bin/env python

n = 20

# soluton 1: A(2n)/A(n)^2
A = lambda n: reduce(lambda x, y: x*y, [i for i in range(1,n+1)])
print A(n*2) / (A(n)**2)

# solution 2: simply A(2n)/A(n)^2
# solution 3: C(40, 20)
mult1 = n+1
mult2 = 1
for i in range(1, n+1):
    mult1 *= i+n
    mult2 *= i+1
print mult1/mult2
