#!/usr/bin/env python

from math import sqrt

f = open('p102_triangles.txt')
triangles = f.read().strip().split()
f.close()

triangles = map(lambda x: map(int, tuple(x.split(','))), triangles)

# use Heron's formula: http://mathworld.wolfram.com/HeronsFormula.html
# area = sqrt(p*(p-a)*(p-b)*(p-c)) = sqrt(4a^2b^2-(a^2+b^2-c^2))/4
cnt = 0
for t in triangles:
    a_sqr = (t[0]-t[2])**2 + (t[1]-t[3])**2
    b_sqr = (t[2]-t[4])**2 + (t[3]-t[5])**2
    c_sqr = (t[4]-t[0])**2 + (t[5]-t[1])**2
    area = sqrt(4*a_sqr*b_sqr - (a_sqr+b_sqr-c_sqr)**2) # real_area*4

    m = t[0]**2 + t[1]**2
    n = t[2]**2 + t[3]**2
    o = t[4]**2 + t[5]**2

    area0 = sqrt(4*m*n - (m+n-a_sqr)**2)
    area1 = sqrt(4*n*o - (n+o-b_sqr)**2)
    area2 = sqrt(4*o*m - (o+m-c_sqr)**2)
    if area0 + area1 + area2 > area:
        continue

    cnt += 1
print cnt
