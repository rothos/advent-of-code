text = open("input20.txt", 'r').read()
# text = open("input20test.txt", 'r').read()

import numpy as np
import heapq
import collections
from functools import cache

grid = np.array([list(l) for l in text.split('\n')])

def shortest_path(grid, start, is_end_fn, get_neighbors_fn):
    seen = set()
    queue = [(0, (start, [start]))]
    while queue:
        cost, (node, path) = heapq.heappop(queue)
        if node not in seen:
            seen.add(node)
            if is_end_fn(node):
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

def do_part(part):

    def is_end_fn(node):
        return node == end

    W,_ = grid.shape
    start = tuple(np.argwhere(grid == 'S')[0])
    end = tuple(np.argwhere(grid == 'E')[0])
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    pathtiles = [tuple(p) for p in np.argwhere(grid == '.')]

    # candidates = set()

    # for pathtile in pathtiles:
    #     for direction in directions:
    #         tile = add(pathtile, direction)
    #         if grid[tile] == '#' and grid[add(tile, direction)] == '.':
    #             candidates += (pathtile, add(tile, direction))

    candidates = set([add(p,direction) for p in pathtiles for direction in directions if grid[*add(p,direction)] == '#'])
    candidates -= set(c for c in candidates if c[0] == 0 or c[1] == 0 or c[0] == W-1 or c[1] == W-1)
    _,best_len = shortest_path(grid, start, is_end_fn, get_neighbors_fn)

    better_lens = collections.defaultdict(int)

    if part == 1:
        for i,candidate in enumerate(candidates):
            grid[*candidate] = '.'
            _,new_len = shortest_path(grid, start, is_end_fn, get_neighbors_fn)
            if new_len < best_len:
                better_lens[new_len] += 1
            grid[*candidate] = '#'

            print(i, '/', len(candidates))

        return sum(better_lens[k] for k in better_lens.keys() if best_len-k >= 100)

    else:
        pass


import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
# start = time.perf_counter()
# print(do_part(2))
# print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
