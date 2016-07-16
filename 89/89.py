#!/usr/bin/env python

f = open('p089_roman.txt')
numbers = f.read()
f.close()
numbers = numbers.split()

cl = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
vd = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

def saved_by_minimal(n):
    v = 0
    for i, c in enumerate(n[:-1]):
        if vd[c] < vd[n[i+1]]:
            v -= vd[c]
        else:
            v += vd[c]
    v += vd[n[-1]]
    x = v

    minimal = ''
    # thousand
    thousand = v / 1000
    minimal += 'M' * thousand
    v = v % 1000

    # hundred
    hundred = v / 100
    if hundred == 9:
        minimal += 'CM'
    elif hundred >= 5:
        minimal += 'D' + 'C' * (hundred-5)
    elif hundred == 4:
        minimal += 'CD'
    else:
        minimal += 'C' * hundred
    v = v % 100

    # ten
    ten = v / 10
    if ten == 9:
        minimal += 'XC'
    elif ten >= 5:
        minimal += 'L' + 'X' * (ten-5)
    elif ten == 4:
        minimal += 'XL'
    else:
        minimal += 'X' * ten
    v = v % 10

    # the last digit
    if v == 9:
        minimal += 'IX'
    elif v >= 5:
        minimal += 'V' + 'I' * (v-5)
    elif v == 4:
        minimal += 'IV'
    else:
        minimal += 'I' * v

    return len(n) - len(minimal)

cnt = 0
for n in numbers:
    cnt += saved_by_minimal(n)
print cnt
