from math import prod, floor, ceil
from collections import Counter, defaultdict
from itertools import permutations, combinations
import re
from functools import cache

import time
time0 = time.time()


file = "input16.txt"
file = "test16.txt"

### PART 1

with open(file, 'r') as f:
    content = f.read()
    grid = [list(l) for l in content.split("\n")]

# energized non-empty tiles (mirrors and splitters)
energized_things = set()
energized = set()

def in_bounds(coord):
    return coord[0] >= 0 and coord[0] < len(grid) and coord[1] >= 0 and coord[1] <= len(grid[0])

def move(coord, direction):
    return (coord[0] + direction[0], coord[1] + direction[1])

def move_reverse(coord, direction):
    return (coord[0] - direction[0], coord[1] - direction[1])

def tile_at(coord):
    return grid[coord[0]][coord[1]]

@cache
def go(coord, direction):
    # Add this tile to energized set
    energized.add(coord)

    print_grid()
    
    # Look in the direction we're going until we hit either
    # a Thing or a wall:
    while in_bounds(coord) and grid[coord[0]][coord[1]] not in "\\/|-":
        energized.add(coord)
        coord = move(coord, direction)

    # We hit a wall
    if not in_bounds(coord):
        return

    tile = tile_at(coord)

    # We have hit a Thing. If we've seen it before, we're done.
    if (tile in "|-" and coord in energized_things) \
        or (tile in "\\/" and tile_at(move_reverse(coord,direction)) in energized and coord in energized_things):
            return

    # Add it to energized things and continue
    energized_things.add(coord)
    energized.add(coord)

    print(len(energized))

    if direction == (0,1) and tile == "-":
        go(move(coord,direction),direction)
    if direction == (0,1) and tile == "|":
        go(move(coord,(-1,0)),(-1,0))
        go(move(coord,(1,0)),(1,0))
    if direction == (0,1) and tile == "\\":
        go(move(coord,(1,0)),(1,0))
    if direction == (0,1) and tile == "/":
        go(move(coord,(-1,0)),(-1,0))

    if direction == (0,-1) and tile == "-":
        go(move(coord,direction),direction)
    if direction == (0,-1) and tile == "|":
        go(move(coord,(-1,0)),(-1,0))
        go(move(coord,(1,0)),(1,0))
    if direction == (0,-1) and tile == "\\":
        go(move(coord,(-1,0)),(-1,0))
    if direction == (0,-1) and tile == "/":
        go(move(coord,(1,0)),(1,0))

    if direction == (1,0) and tile == "-":
        go(move(coord,(0,-1)),(0,-1))
        go(move(coord,(0,1)),(0,1))
    if direction == (1,0) and tile == "|":
        go(move(coord,direction),direction)
    if direction == (1,0) and tile == "\\":
        go(move(coord,(0,1)),(0,1))
    if direction == (1,0) and tile == "/":
        go(move(coord,(0,-1)),(0,-1))

    if direction == (-1,0) and tile == "-":
        go(move(coord,(0,-1)),(0,-1))
        go(move(coord,(0,1)),(0,1))
    if direction == (-1,0) and tile == "|":
        go(move(coord,direction),direction)
    if direction == (-1,0) and tile == "\\":
        go(move(coord,(0,-1)),(0,-1))
    if direction == (-1,0) and tile == "/":
        go(move(coord,(0,1)),(0,1))

    return

def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) in energized:
                print("#", end="")
            else:
                print(grid[i][j], end="")
        print()
    print()

go((0,0), (0,1))

print(len(energized))
print()
# print(energized)
# print(energized_things)

# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if (i,j) in energized:
#             print("#", end="")
#         else:
#             print(grid[i][j], end="")
#     print()
# print()
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if (i,j) in energized_things:
#             print("#", end="")
#         else:
#             print(grid[i][j], end="")
#     print()
