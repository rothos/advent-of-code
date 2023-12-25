from math import prod, floor, ceil
from collections import Counter, defaultdict
from itertools import permutations, combinations
import re
from functools import cache

import time
time0 = time.time()


file = "input16.txt"
# file = "test16.txt"

### PART 1

with open(file, 'r') as f:
    content = f.read()
    grid = [list(l) for l in content.split("\n")]

# # energized non-empty tiles (mirrors and splitters)
# energized_things = set()
# energized = set()

def in_bounds(coord):
    return (0 <= coord[0] < len(grid)) and (0 <= coord[1] < len(grid[0]))

def move(coord, direction):
    return (coord[0] + direction[0], coord[1] + direction[1])

def move_reverse(coord, direction):
    return (coord[0] - direction[0], coord[1] - direction[1])

def tile_at(coord):
    return grid[coord[0]][coord[1]]

# @cache
def go(coord, direction, ee=None, eex=None):
    if not ee:
        ee = set()

    if not eex:
        eex = set()

    if not in_bounds(coord):
        return ee,eex

    # Add this tile to ee set
    ee.add(coord)

    # Look in the direction we're going until we hit either
    # a Thing or a wall:
    while in_bounds(coord) and grid[coord[0]][coord[1]] not in "\\/|-":
        ee.add(coord)
        coord = move(coord, direction)

    # We hit a wall
    if not in_bounds(coord):
        return ee,eex

    tile = tile_at(coord)

    # We have hit a Thing. If we've seen it before, we're done.
    if (tile in "|-" and coord in eex) \
        or (tile in "\\/" \
            and in_bounds(move_reverse(coord,direction)) \
            and tile_at(move_reverse(coord,direction)) in ee and coord in eex):
                return ee,eex

    # Add it to ee things and continue
    eex.add(coord)
    ee.add(coord)

    if direction == (0,1) and tile == "-":
        ee,eex = go(move(coord,direction),direction,ee,eex)
    if direction == (0,1) and tile == "|":
        ee,eex = go(move(coord,(-1,0)),(-1,0),ee,eex)
        ee,eex = go(move(coord,(1,0)),(1,0),ee,eex)
    if direction == (0,1) and tile == "\\":
        ee,eex = go(move(coord,(1,0)),(1,0),ee,eex)
    if direction == (0,1) and tile == "/":
        ee,eex = go(move(coord,(-1,0)),(-1,0),ee,eex)

    if direction == (0,-1) and tile == "-":
        ee,eex = go(move(coord,direction),direction,ee,eex)
    if direction == (0,-1) and tile == "|":
        ee,eex = go(move(coord,(-1,0)),(-1,0),ee,eex)
        ee,eex = go(move(coord,(1,0)),(1,0),ee,eex)
    if direction == (0,-1) and tile == "\\":
        ee,eex = go(move(coord,(-1,0)),(-1,0),ee,eex)
    if direction == (0,-1) and tile == "/":
        ee,eex = go(move(coord,(1,0)),(1,0),ee,eex)

    if direction == (1,0) and tile == "-":
        ee,eex = go(move(coord,(0,-1)),(0,-1),ee,eex)
        ee,eex = go(move(coord,(0,1)),(0,1),ee,eex)
    if direction == (1,0) and tile == "|":
        ee,eex = go(move(coord,direction),direction,ee,eex)
    if direction == (1,0) and tile == "\\":
        ee,eex = go(move(coord,(0,1)),(0,1),ee,eex)
    if direction == (1,0) and tile == "/":
        ee,eex = go(move(coord,(0,-1)),(0,-1),ee,eex)

    if direction == (-1,0) and tile == "-":
        ee,eex = go(move(coord,(0,-1)),(0,-1),ee,eex)
        ee,eex = go(move(coord,(0,1)),(0,1),ee,eex)
    if direction == (-1,0) and tile == "|":
        ee,eex = go(move(coord,direction),direction,ee,eex)
    if direction == (-1,0) and tile == "\\":
        ee,eex = go(move(coord,(0,-1)),(0,-1),ee,eex)
    if direction == (-1,0) and tile == "/":
        ee,eex = go(move(coord,(0,1)),(0,1),ee,eex)

    return ee,eex

def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) in energized:
                print("#", end="")
            else:
                print(grid[i][j], end="")
        print()
    print()


# PART 1
energized,_ = go((0,0), (0,1))
print(len(energized))
# 6740

time1 = time.time()
print("%.3fs" % (time1-time0))


# PART 2
ans = -1
for i in range(len(grid)):
    q,_ = go((i,0),(0,1))
    ans = max(ans, len(q))
    q,_ = go((i,len(grid)-1),(0,-1))
    ans = max(ans, len(q))

for j in range(len(grid[0])):
    q,_ = go((0,j),(1,0))
    ans = max(ans, len(q))
    q,_ = go((len(grid[0])-1,j),(-1,0))
    ans = max(ans, len(q))

print(ans)
# 7041

time2 = time.time()
print("%.3fs" % (time2-time1))
