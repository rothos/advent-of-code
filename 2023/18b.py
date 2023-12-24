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

# mm = {"U":(0,1), "D":(0,-1), "L":(-1,0), "R":(1,0)}
mm = {3:(0,1), 1:(0,-1), 2:(-1,0), 0:(1,0)}

pos = (0,0)
pts = [pos]
for d,l in dirs:
    if d == 0: pos = (pos[0]+l, pos[1])
    if d == 1: pos = (pos[0], pos[1]+l)
    if d == 2: pos = (pos[0]-l, pos[1])
    if d == 3: pos = (pos[0], pos[1]-l)
    pts += [pos]

xx = sorted(list(set(p[0] for p in pts)))
yy = sorted(list(set(p[1] for p in pts)))

pos = (0,0)
compressedpts = [pos]
for d,l in dirs:
    if d == 0: pos = (pos[0]+l, pos[1])
    if d == 1: pos = (pos[0], pos[1]+l)
    if d == 2: pos = (pos[0]-l, pos[1])
    if d == 3: pos = (pos[0], pos[1]-l)
    x,y = xx.index(pos[0]), yy.index(pos[1])
    compressedpts += [(x,y)]

print(pts)
print(compressedpts)
exit()









def addpts(a,b,repeat=1):
    return (a[0]+repeat*b[0], a[1]+repeat*b[1])

def bounds(pts):
    x0 = min(p[0] for p in pts)
    x1 = max(p[0] for p in pts)
    y0 = min(p[1] for p in pts)
    y1 = max(p[1] for p in pts)
    return (x0,x1,y0,y1)

cur = (0,0)
pts = set()
for line in lines:
    direction,length,color = line
    step = mm[direction]
    for _ in range(length):
        cur = addpts(cur,step)
        pts.add(cur)

pts_interior = set()

x0,x1,y0,y1 = bounds(pts)
for x in range(x0,x1+1):
    inside = False
    onedge = False
    direction = None
    lastdirection = None
    for y in range(y0,y1+1):
        if (x,y) in pts:
            if not onedge:
                if ((x-1,y) in pts) ^ ((x+1,y) in pts):
                    direction = (x-1,y) in pts
            if ((x-1,y) in pts) ^ ((x+1,y) in pts):
                lastdirection = (x-1,y) in pts

            onedge = True

        else:
            if onedge and ((direction == None) or (direction != lastdirection)):
                inside = not inside

            direction = None
            lastdirection = None
            onedge = False

            if inside:
                pts_interior.add((x,y))

print(len(pts) + len(pts_interior))

time1 = time.time()
print("%.3fms" % (time1-time0))
