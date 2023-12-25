from math import prod, floor, ceil
from collections import Counter, defaultdict
from itertools import permutations, combinations
import re
from functools import cache

import time
time0 = time.time()

file = "input18.txt"
# file = "test18.txt"

lines = open(file).read().split("\n")
lines = [l.split("#")[1][:-1] for l in lines]
dirs = [(int(l[-1]), int(l[:-1],16)) for l in lines]

def shoelace(pts):
    total = 0
    for i in range(len(pts)):
        a = pts[i]
        b = pts[(i+1)%len(pts)]
        total += a[0]*b[1] - a[1]*b[0]
        total += abs(a[0]-b[0]) + abs(a[1]-b[1])
    return total//2 + 1

pos = (0,0)
pts = []
for d,l in dirs:
    if d == 0: pos = (pos[0]+l, pos[1])
    if d == 1: pos = (pos[0], pos[1]+l)
    if d == 2: pos = (pos[0]-l, pos[1])
    if d == 3: pos = (pos[0], pos[1]-l)
    pts += [pos]

print(shoelace(pts))
