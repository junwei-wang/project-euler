#!/usr/bin/env python

f = open('./p022_names.txt')
names = f.read()
f.close

names = sorted(names.split(","))

sum = 0
for i, name in enumerate(names):
    num = reduce(lambda x, y: x+y, map(lambda c: ord(c)-64, name[1:-1]))
    sum += num*(i+1)
    if name == '"COLIN"':
        print num, i+1

print sum
