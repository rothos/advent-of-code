text = open("input18.txt", 'r').read(); W = 71; N = 1024
# text = open("input18test.txt", 'r').read(); W = 7; N = 12

import numpy as np
import heapq

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

def is_end_fn(node):
    return node[0] == W-1 and node[1] == W-1

def get_neighbors_fn(grid, node):
    x,y = node
    neighbors = []
    if x+1 < W and grid[(x+1,y)]: neighbors.append(((x+1,y), 1))
    if x-1 >= 0 and grid[(x-1,y)]: neighbors.append(((x-1,y), 1))
    if y+1 < W and grid[(x,y+1)]: neighbors.append(((x,y+1), 1))
    if y-1 >= 0 and grid[(x,y-1)]: neighbors.append(((x,y-1), 1))
    return neighbors

def do_part(part):
    byts = [(int(l.split(",")[0]), int(l.split(",")[1])) for l in text.splitlines()]
    grid = np.ones([W,W])
    for pt in byts[:N]:
        grid[pt[::-1]] = 0

    x0,y0 = 0,0
    x1,y1 = W,W

    if part == 1:
        path,cost = shortest_path(grid, (0,0), is_end_fn, get_neighbors_fn)
        return len(path)-1

    else:
        for pt in byts[N:]:
            grid[pt[::-1]] = 0
            try:
                path,cost = shortest_path(grid, (0,0), is_end_fn, get_neighbors_fn)
            except:
                return ",".join(str(x) for x in pt)

import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
