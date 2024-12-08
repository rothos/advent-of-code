text = open("input8.txt", 'r').read()
# text = open("input8test.txt", 'r').read()


import numpy as np
import itertools

def in_grid(coord, grid):
    w,h = grid.shape
    return 0 <= coord[0] < w and 0 <= coord[1] < h

def get_antinodes(a, b, grid, part2):
    ants = set()
    k = 1
    while in_grid( k*(b-a)+a, grid ) and (part2 or k < 3):
        if part2 or k == 2:
            ants.add(tuple(k*(b-a)+a))
        k+=1

    return ants


types = set(text).difference({'\n', '.'})
grid = np.array([list(t) for t in text.splitlines()])

def day8(part2=False):
    antinodes = set()
    for type in types:
        ants = np.argwhere(grid == type)
        for a,b in itertools.combinations(ants, 2):
            antinodes = antinodes.union(get_antinodes(a, b, grid, part2))
            antinodes = antinodes.union(get_antinodes(b, a, grid, part2))

    return len(antinodes)


print(day8())
print(day8(part2=True))
