#!/usr/bin/env python

from math import sqrt, ceil

f = open('p042_words.txt')
words = f.read()
f.close

words = map(lambda x: x[1:-1], words.split(','))
max_len = len(max(words, key=len))
max_val = 26 * max_len

l = [i*(i+1)/2 for i in range(1, int(sqrt(max_val*2))+2)]



def is_triangle_word(word):
    v = map(lambda c: ord(c)-64, word)
    return sum(v) in l

cnt = 0
for w in words:
    if is_triangle_word(w):
        cnt += 1

print cnt
