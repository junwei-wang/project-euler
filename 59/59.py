#!/usr/bin/env python

f = open('p059_cipher.txt')
ciphers = f.read()
f.close()
ciphers = map(int, ciphers.strip().split(','))

first = dict()
second = dict()
third = dict()
for i in range(0, len(ciphers)-3, 3):
    v = ciphers[i]
    first[v] = first[v] + 1 if v in first else 1
    v = ciphers[i+1]
    second[v] = second[v] + 1 if v in second else 1
    v = ciphers[i+2]
    third[v] = third[v] + 1 if v in third else 1

first = 32 + max(first.iteritems(), key=lambda x: x[1])[0]
second = 32 + max(second.iteritems(), key=lambda x: x[1])[0]
third = 32 + max(third.iteritems(), key=lambda x: x[1])[0]

result = 0
for i, v in enumerate(ciphers):
    if i % 3 == 0:
        result += v ^ first
    elif i % 3 == 1:
        result += v ^ second
    else:
        result += v ^ third

print result
