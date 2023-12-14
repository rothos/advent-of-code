from math import prod, floor, ceil
from collections import Counter, defaultdict
from itertools import permutations, combinations
import re

import time
time0 = time.time()


file = "input14.txt"
# file = "test14.txt"

### PART 1

with open(file, 'r') as f:
    content = f.read()
    lines = [list(l) for l in content.split("\n")]


def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def slug(field):
    return "".join("".join(s) for s in field)

# 0 = north
# 1 = west
# 2 = south
# 3 = east
def roll(field, direction=0):
    if direction == 1:
        field = transpose(field)
    if direction == 2:
        field = field[::-1]
    if direction == 3:
        field = transpose(field)[::-1]

    changed = True
    while changed:
        changed = False
        for i in range(1,len(field)):
            for j in range(len(field[0])):
                if field[i][j] == "O" and field[i-1][j] == ".":
                    field[i][j] = "."
                    field[i-1][j] = "O"
                    changed = True

    if direction == 1:
        field = transpose(field)
    if direction == 2:
        field = field[::-1]
    if direction == 3:
        field = transpose(field[::-1])

    return field

def load(field):
    t = 0
    for i,line in enumerate(field):
        t += (len(field)-i)*sum(c=="O" for c in line)
    return t



#### PART 1

t = 0
rolled = roll(lines)
for i,line in enumerate(rolled):
    t += (len(rolled)-i)*sum(c=="O" for c in line)

ans = t
time1 = time.time()
print(ans, " ", "%.3f seconds" % (time1 - time0))


### PART 2

d = defaultdict(list)

for h in range(1,10000):
    for direction in range(4):
        lines = roll(lines, direction)

    d[slug(lines)] += [h]
    if max(len(v) for v in d.values()) > 1:
        cycle = d[slug(lines)][1] - d[slug(lines)][0]
        break

mod = int((1e9-h) % cycle) + h

for c in range(h+1,mod+1):
    for direction in range(4):
        lines = roll(lines, direction)

ans = load(lines)
time2 = time.time()
print(ans, " ", "%.3f seconds" % (time2 - time1))
