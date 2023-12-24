from math import prod, floor, ceil
from collections import Counter, defaultdict
from itertools import permutations, combinations
import re
from functools import cache

import time
time0 = time.time()

file = "input18.txt"
file = "test18.txt"

with open(file, 'r') as f:
    content = f.read()
    lines = content.split("\n")
    lines = [l.split("#")[1][:-1] for l in lines]
    dirs = [(int(l[-1]), int(l[:-1],16)) for l in lines]

# Example
dirs = [(0,6),(1,5),(2,2),(1,2),(0,2),(1,2),(2,5),(3,2),(2,1),(3,2),(0,2),(3,3),(2,2),(3,2)]

# Translate the absolute directions into relative ones.
# Here the first number in the tuple is -1 (left turn) or 1 (right turn).
turns = []
curdir = 3
for d,l in dirs:
    turns.append(( 2-((d-curdir)%4), l ))
    curdir = d

halfs = []
# Now modify the directions to move through half-integers
# just outside of the actual path.
for i,(t,l) in enumerate(turns):
    nextturn = turns[(i+1)%len(turns)][0]
    correction = t if t==nextturn else 0
    halfs.append((t, l+correction))

# Now get the absolute xy coordinates of the (half-integer) corners
coords = [(-0.5,-0.5)]
d = 3
for t,l in halfs:
    d = (t-d)%4
    pos = list(coords[-1])
    pos[d%2] = pos[d%2] + l*[-1,1][d<2]
    coords += [tuple(pos)]

M = dict()



print(coords)
# print(turns)
# print(halfs)




time1 = time.time()
print("%.3fms" % (time1-time0))
