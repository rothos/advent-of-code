text = open("input20.txt", 'r').read(); test = 0
# text = open("input20test.txt", 'r').read(); test = 1

import numpy as np
import heapq
import collections
from functools import cache

def build_map(grid, cur, end):
    seen = set(cur)
    path_map = dict()
    path_map[cur] = 0
    i = 1
    not_to_end = True
    while not_to_end:
        for direction in [(0,-1), (0,1), (-1,0), (1,0)]:
            nex = (cur[0]+direction[0], cur[1]+direction[1])
            if nex not in seen and grid[nex] != "#":
                path_map[nex] = i
                seen.add(nex)
                if nex == end:
                    not_to_end = False
                i += 1
                cur = nex
                break

    return path_map

def get_path_tiles_within_N_steps(start, pathtiles, N):
    results = set()
    for pathtile in pathtiles:
        diff = abs(start[0] - pathtile[0]) + abs(start[1] - pathtile[1])
        if 1 < diff <= N:
            results.add((pathtile, diff))

    return results

def print_grid(grid):
    print("\n".join("".join(row) for row in grid))

def do_part(part):
    grid = np.array([list(l) for l in text.split('\n')])
    start = tuple(np.argwhere(grid == 'S')[0])
    end = tuple(np.argwhere(grid == 'E')[0])
    path_map = build_map(grid, start, end)
    pathtiles = [tuple(pt) for pt in np.argwhere(grid == '.')] + [start] + [end]

    goal_saved = 100 if not test else 10
    allowed_cheat_len = 2 if part == 1 else 20

    seen = set()
    picoseconds_saved = collections.defaultdict(int)

    for pathtile in pathtiles:
        candidates = get_path_tiles_within_N_steps(pathtile, pathtiles, allowed_cheat_len)

        for cheattile,cheatlen in candidates:
            hashed_cheat = tuple(sorted([pathtile, cheattile]))

            if hashed_cheat in seen:
                continue

            saved = abs(path_map[cheattile] - path_map[pathtile])
            picoseconds_saved[saved - cheatlen] += 1
            seen.add(hashed_cheat)

    return sum([picoseconds_saved[k] for k in picoseconds_saved.keys() if k >= goal_saved])

import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
