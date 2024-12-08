text = open("input8.txt", 'r').read()
# text = open("input8test.txt", 'r').read()


import numpy as np
import itertools

def in_grid(coord, grid):
    w,h = grid.shape
    return 0 <= coord[0] < w and 0 <= coord[1] < h

types = set(text).difference({'\n', '.'})
grid = np.array([list(t) for t in text.splitlines()])

def day8(part2=False):
    antinodes = set()
    for type in types:
        ants = np.argwhere(grid == type)
        for a,b in itertools.combinations(ants, 2):
            if part2:
                k = 1
                while in_grid( k*(b-a)+a, grid ):
                    antinodes.add(tuple(k*(b-a)+a))
                    k+=1
                k = 1
                while in_grid( k*(a-b)+b, grid ):
                    antinodes.add(tuple(k*(a-b)+b))
                    k+=1

            else:
                an1 = 2*b - a
                an2 = 2*a - b
                if in_grid(an1, grid):
                    antinodes.add(tuple(an1))
                if in_grid(an2, grid):
                    antinodes.add(tuple(an2))

    return len(antinodes)


print(day8())
print(day8(part2=True))
