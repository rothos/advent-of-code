text = open("input16.txt", 'r').read()
text = open("input16test2.txt", 'r').read()
# text = open("input16test.txt", 'r').read()

import numpy as np
import heapq

def shortest_path(start, is_end, neighbors_function):
    seen = set()
    queue = [(0, (start, [start]))]
    while queue:
        cost, (node, path) = heapq.heappop(queue)
        if node not in seen:
            seen.add(node)
            if is_end(node):
                return path,cost
            for neighbor,thiscost in neighbors_function(node):
                heapq.heappush(queue, (cost + thiscost, (neighbor, path + [neighbor])))

def all_shortest_paths(start, is_end, neighbors_function):
    seen = {}
    queue = [(0, (start, [start]))]
    best_cost = float('inf')
    all_optimal_paths = []

    while queue:
        cost, (node, path) = heapq.heappop(queue)
        if cost > best_cost:
            break

        if (node not in seen or cost <= seen[node]):
            seen[node] = cost
            
            if is_end(node):
                if not all_optimal_paths or cost <= best_cost:
                    if cost < best_cost:
                        all_optimal_paths = []
                        best_cost = cost

                    all_optimal_paths.append(path)
            
            for neighbor, thiscost in neighbors_function(node):
                new_cost = cost + thiscost
                if new_cost <= best_cost:
                    heapq.heappush(queue, (new_cost, (neighbor, path + [neighbor])))
    
    return all_optimal_paths, best_cost

def xy_only(nodes):
    xyset = set()
    for node in nodes:
        xyset.add(node[0])
    return xyset

def is_end(end_xy):
    return lambda node: node[0] == end_xy

def add(a,b):
    return (a[0]+b[0], a[1]+b[1])

def rot90(direction):
    if direction == (0,1):  return (1,0)
    if direction == (1,0):  return (0,-1)
    if direction == (0,-1): return (-1,0)
    if direction == (-1,0): return (0,1)

def get_neighbors(grid):
    def _get_neighbors(node):
        neighbors = []
        # Can either turn or go forward
        xy,direction = node
        neighbors.append( ((xy, rot90(direction)), 1000) )
        neighbors.append( ((xy, rot90(rot90(direction))), 1000) )
        neighbors.append( ((xy, rot90(rot90(rot90(direction)))), 1000) )

        if grid[xy] != "#":
            neighbors.append( ((add(xy, direction), direction), 1) )

        return neighbors

    return _get_neighbors

def do_part(part):
    grid = np.array([list(l) for l in text.split('\n')])
    start_xy = tuple(np.argwhere(grid == "S")[0])
    end_xy = tuple(np.argwhere(grid == "E")[0])
    direction = (0,1)

    if part == 1:
        start = (start_xy, direction)
        path,cost = shortest_path(start, is_end(end_xy), get_neighbors(grid))
        return cost

    else:
        start = (start_xy, direction)
        all_paths, cost = all_shortest_paths(start, is_end(end_xy), get_neighbors(grid))
        tiles = set()
        for path in all_paths:
            for node in path:
                tiles.add(node[0])
        return len(tiles)

import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
