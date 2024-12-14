test = 0

if test:
    lines = open("input14test.txt", 'r').read().splitlines()
    w,h = 11,7
else:
    lines = open("input14.txt", 'r').read().splitlines()
    w,h = 101,103


### PART 1

import numpy as np
import re
from math import prod


import time
start = time.perf_counter()
t = 100
quads = [0,0,0,0]

for line in lines:
    pos, vel = [np.array(re.findall(r'-?\d+', part), dtype=int) for part in line.split()]
    x,y = ( (pos + vel*t) % [w,h] ) - np.array([w-1,h-1])//2
    if   x > 0 and y > 0: quads[0] += 1
    elif x > 0 and y < 0: quads[1] += 1
    elif x < 0 and y > 0: quads[2] += 1
    elif x < 0 and y < 0: quads[3] += 1


print(prod(quads))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")


### PART 2

def has_run(grid, run_length=10):
    kernel = np.ones(run_length, dtype=int)
    for row in grid:
        convolved = np.convolve(row, kernel, mode='valid')
        if np.any(convolved == run_length):
            return True
    return False

def print_grid(grid):
    for row in grid:
        print(''.join('X' if val else '.' for val in row))

start = time.perf_counter()
t = 0
while True:
    grid = np.full([w,h], False)
    for line in lines:
        pos, vel = [np.array(re.findall(r'-?\d+', part), dtype=int) for part in line.split()]
        x,y = ( (pos + vel*t) % [w,h] )
        grid[x,y] = True

    if has_run(grid):
        # print_grid(grid)
        print(t)
        break

    t += 1

print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
