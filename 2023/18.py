from math import prod, floor, ceil
from collections import Counter, defaultdict
from itertools import permutations, combinations
import re
from functools import cache

import time
time0 = time.time()

file = "input18.txt"
# file = "test18.txt"

with open(file, 'r') as f:
    content = f.read()
    lines = content.split("\n")
    lines = [l.split() for l in lines]
    lines = [(l[0], int(l[1]), l[2][2:-1]) for l in lines]

mm = {"U":(0,1), "D":(0,-1), "L":(-1,0), "R":(1,0)}

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
    direction = None
    lastdirection = None
    for y in range(y0,y1+1):
        if (x,y) in pts:
            if not inside:
                if ((x-1,y) in pts) ^ ((x+1,y) in pts):
                    direction = (x-1,y) in pts
            if ((x-1,y) in pts) ^ ((x+1,y) in pts):
                lastdirection = (x-1,y) in pts
            
            inside = (x,y-1) not in pts_interior

        elif inside:
            # print(x,y,direction,lastdirection)
            if direction != None and direction == lastdirection:
                inside = False
                continue

            direction = None
            lastdirection = None
            pts_interior.add((x,y))


x0,x1,y0,y1 = bounds(pts)
for y in range(y0,y1+1):
    for x in range(x0,x1+1):
        if (x,y) in pts:
            print("#",end="")
        elif (x,y) in pts_interior:
            print("o",end="")
        else:
            print(".",end="")
    print()



print(len(pts))
print(len(pts) + len(pts_interior))
# 52460 (too high)

# print(sorted(list(pts)))


time1 = time.time()
print("%.3fms" % (time1-time0))
