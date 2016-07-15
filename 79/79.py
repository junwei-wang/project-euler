#!/usr/bin/env python

f = open('p079_keylog.txt')
keys = f.read()
f.close()

keys = set(keys.split())
# keys = sorted(map(int, keys))

res = list()


# the fisrt
m = dict()
for k in keys:
    if k[0] in m:
        m[k[0]] += 1
    else:
        m[k[0]] = 1
res.append(max(m, key=m.get))
keys = [k[1:] if k[0] == res[-1] else k for k in keys]
keys = set([k for k in keys if k])

# the second
m = dict()
for k in keys:
    if k[0] in m:
        m[k[0]] += 1
    else:
        m[k[0]] = 1
res.append(max(m, key=m.get))
keys = [k[1:] if k[0] == res[-1] else k for k in keys]
keys = set([k for k in keys if k])

# the third
m = dict()
for k in keys:
    if k[0] in m:
        m[k[0]] += 1
    else:
        m[k[0]] = 1
res.append(max(m, key=m.get))
keys = [k[1:] if k[0] == res[-1] else k for k in keys]
keys = set([k for k in keys if k])

# the forth
m = dict()
for k in keys:
    if k[0] in m:
        m[k[0]] += 1
    else:
        m[k[0]] = 1
res.append(max(m, key=m.get))
keys = [k[1:] if k[0] == res[-1] else k for k in keys]
keys = set([k for k in keys if k])

# the forth
m = dict()
for k in keys:
    if k[0] in m:
        m[k[0]] += 1
    else:
        m[k[0]] = 1
res.append(max(m, key=m.get))
keys = [k[1:] if k[0] == res[-1] else k for k in keys]
keys = set([k for k in keys if k])

print ''.join(res)
print keys
