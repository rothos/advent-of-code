lines = open("input12.txt", 'r').read().splitlines()
# lines = open("input12test.txt", 'r').read().splitlines()

from functools import cache
import numpy as np

NEIGHBORS = [(0,-1), (0,1), (-1,0), (1,0)]

grid = np.array([list(l) for l in lines])
grid = np.pad(grid, 1, constant_values='.')
types = np.unique(grid)

total = 0

def fill_region(grid, pt):
    region = set()
    area = 0
    boundary = 0
    croptype = grid[tuple(pt)]

    add_pts = lambda x,y: (x[0]+y[0], x[1]+y[1])

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


total = 0
checked = set()
h,w  = grid.shape
for i in range(h):
    for j in range(w):
        pt = (i, j)
        if pt not in checked and grid[pt] != '.':
            area, boundary, region = fill_region(grid, pt)
            checked |= region
            total += area * boundary

print(total)
