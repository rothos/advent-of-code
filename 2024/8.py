text = open("input8.txt", 'r').read()
# text = open("input8test.txt", 'r').read()


import numpy as np
import itertools

def in_grid(coord, grid):
    w,h = grid.shape
    return 0 <= coord[0] < w and 0 <= coord[1] < h

def get_antinodes(a, b, grid, part2):
    if not part2:
        return {tuple(2*b-a)} if in_grid(2*b-a, grid) else set()

    antinodes, k = set(), 1
    while in_grid( k*(b-a)+a, grid ):
        antinodes.add(tuple(k*(b-a)+a))
        k += 1

    return antinodes

def day8(part2=False):
    antinodes = set()
    for type in types:
        antennas = np.argwhere(grid == type)
        for a,b in itertools.combinations(antennas, 2):
            antinodes = antinodes.union(get_antinodes(a, b, grid, part2))
            antinodes = antinodes.union(get_antinodes(b, a, grid, part2))

    return len(antinodes)

types = set(text).difference({'\n', '.'})
grid = np.array([list(t) for t in text.splitlines()])

print(day8())
print(day8(part2=True))
