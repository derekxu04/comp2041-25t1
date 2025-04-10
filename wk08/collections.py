#!/usr/bin/env python3

from collections import Counter, defaultdict, OrderedDict

l = [1, 2, 3, 4, 1, 5, 6, 7, 7, 7, 8, 9, 10]

# Using dictionary
d = {}
for i in l:
    if i not in d:
        d[i] = 0
    d[i] += 1

print(d)

# Using Counter
c = Counter(l)
print(c)
print(c.most_common(3))

# Using defaultdict
d = defaultdict(int)
for i in l:
    d[i] += 1
print(d)

d = defaultdict(list)
for i in l:
    d[i].append(i)
print(d)

# Using OrderedDict
d = OrderedDict()
d['b'] = 2
d['a'] = 1
print(d)