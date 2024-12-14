test = 0

if test:
    lines = open("input14test.txt", 'r').read().splitlines()
    w,h = 11,7
else:
    lines = open("input14.txt", 'r').read().splitlines()
    w,h = 101,103


import numpy as np
import re
from math import prod

t = 100
quads = [0,0,0,0]

for line in lines:
    pos, vel = [np.array(re.findall(r'-?\d+', part), dtype=int) for part in line.split()]
    x,y = ( (pos + vel*t) % [w,h] ) - np.array([w-1,h-1])//2
    if x > 0 and y > 0:
        quads[0] += 1
    elif x > 0 and y < 0:
        quads[1] += 1
    elif x < 0 and y > 0:
        quads[2] += 1
    elif x < 0 and y < 0:
        quads[3] += 1

print(prod(quads))


### PART 2

from scipy.stats import entropy

def calculate_entropy(array, window_size):
    h, w = array.shape
    entropies = []
    for i in range(0, h - window_size + 1, window_size):
        for j in range(0, w - window_size + 1, window_size):
            sub_window = array[i:i+window_size, j:j+window_size]
            p_true = np.sum(sub_window) / sub_window.size
            p_false = 1 - p_true
            probabilities = np.array([p_true, p_false])
            entropies.append(entropy(probabilities, base=2))
    return np.mean(entropies)

def print_grid(grid):
    for row in grid:
        print(''.join('X' if val else '.' for val in row))

t = 0
while True:
    if t % 100 == 0:
        print(f't = {t}...')
    grid = np.full([w,h], False)
    for line in lines:
        pos, vel = [np.array(re.findall(r'-?\d+', part), dtype=int) for part in line.split()]
        x,y = ( (pos + vel*t) % [w,h] )
        grid[x,y] = True

    e = calculate_entropy(grid, 5)

    if e < 0.2:
        print_grid(grid)
        # _ = input(f'^ t = {t}')

    t += 1
