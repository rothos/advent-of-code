lines = open("input12.txt", 'r').read().splitlines()
# lines = open("input12test.txt", 'r').read().splitlines()

from functools import cache
import numpy as np

NEIGHBORS = [(0,-1), (0,1), (-1,0), (1,0)]
add_pts = lambda x,y: (x[0]+y[0], x[1]+y[1])

grid = np.array([list(l) for l in lines])
grid = np.pad(grid, 1, constant_values='.')
h,w = grid.shape
types = np.unique(grid)

total = 0

def get_neighbors(pt):
    return [add_pts(pt, n) for n in NEIGHBORS]

def fill_region(grid, pt):
    region = set()
    area = 0
    boundary = 0
    croptype = grid[tuple(pt)]

    to_check = {pt}

    while len(to_check):
        pt = to_check.pop()

        region.add(pt)
        area += 1
        boundary += 4

        for n in NEIGHBORS:
            npt = add_pts(pt, n)

            if npt in region:
                boundary -= 2

            elif grid[npt] == croptype:
                to_check.add(npt)

    return area, boundary, region

def count_sides(region):
    min_i = min(x[0] for x in region)
    min_j = min(x[1] for x in region)
    region = [(x[0]-min_i, x[1]-min_j) for x in region]
    max_i = max(x[0] for x in region) + 1
    max_j = max(x[1] for x in region) + 1

    area = np.zeros((max_i, max_j))
    area[*zip(*region)] = 1
    area = np.pad(area, 1, constant_values=0)

    sides = 0
    for _ in range(4):
        for i in range(1, area.shape[0]):
            row = [area[i,j] and not area[i-1,j] for j in range(area.shape[1])] + [0]
            sides += sum(np.diff(row) < 0)

        area = np.rot90(area)

    return sides

def go():
    total1 = 0
    total2 = 0
    checked = set()
    h,w  = grid.shape
    for i in range(h):
        for j in range(w):
            pt = (i, j)
            if pt not in checked and grid[pt] != '.':
                area, boundary, region = fill_region(grid, pt)
                checked |= region
                total1 += area * boundary
                total2 += area * count_sides(region)
    return total1, total2


import time
start = time.perf_counter()
ans1, ans2 = go()
print(ans1)
print(ans2)
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
