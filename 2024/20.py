text = open("input20.txt", 'r').read()
# text = open("input20test.txt", 'r').read()

import numpy as np
import heapq
import collections
from functools import cache

grid = np.array([list(l) for l in text.split('\n')])

def shortest_path(grid, start, end, get_neighbors_fn):
    seen = set()
    queue = [(0, (start, [start]))]
    while queue:
        cost, (node, path) = heapq.heappop(queue)
        if node not in seen:
            seen.add(node)
            if node == end:
                return path,cost
            for neighbor,move_cost in get_neighbors_fn(grid, node):
                heapq.heappush(queue, (cost + move_cost, (neighbor, path + [neighbor])))
    return None

def get_neighbors_fn(grid, node):
    W,_ = grid.shape
    x,y = node
    neighbors = []
    if x+1 < W and grid[(x+1,y)] != '#': neighbors.append(((x+1,y), 1))
    if x-1 >= 0 and grid[(x-1,y)] != '#': neighbors.append(((x-1,y), 1))
    if y+1 < W and grid[(x,y+1)] != '#': neighbors.append(((x,y+1), 1))
    if y-1 >= 0 and grid[(x,y-1)] != '#': neighbors.append(((x,y-1), 1))
    return neighbors

def add(a,b):
    return (a[0]+b[0], a[1]+b[1])

def negate(v):
    return (-v[0], -v[1])

def in_bounds(pt):
    W,_ = grid.shape
    x,y = pt
    return 0 <= x < W and 0 <= y < W

def get_path_tiles_within_N_steps(start, pathtiles):
    pass

def print_grid(grid):
    print("\n".join("".join(row) for row in grid))

def do_part(part):
    W,_ = grid.shape
    start = tuple(np.argwhere(grid == 'S')[0])
    end = tuple(np.argwhere(grid == 'E')[0])

    best_path, best_len = shortest_path(grid, start, end, get_neighbors_fn)
    best_path_map = dict()
    for i,pt in enumerate(best_path):
        best_path_map[pt] = i

    seen = set()
    pathtiles = [tuple(pt) for pt in np.argwhere(grid == '.')] + [start] + [end]
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    picoseconds_saved = collections.defaultdict(int)

    for pathtile in pathtiles:
        for direction in directions:
            go_one = add(pathtile, direction)
            go_two = add(go_one, direction)

            if go_one in seen or not in_bounds(go_two):
                continue

            if go_one not in pathtiles and go_two in pathtiles:
                diff = abs(best_path_map[go_two] - best_path_map[pathtile])
                picoseconds_saved[diff-2] += 1
                seen.add(go_one)

    if part == 1:
        return sum([picoseconds_saved[k] for k in picoseconds_saved.keys() if k >= 100])

    else:
        pass


import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
# start = time.perf_counter()
# print(do_part(2))
# print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
