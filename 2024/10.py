from functools import cache
import time
start = time.perf_counter()

lines = open("input10.txt", 'r').read().splitlines()
# lines = open("input10test.txt", 'r').read().splitlines()

@cache
def get_neighbors(i, j, chart):
    # returns list of coords of neighbors of i,j
    neighbors = []
    for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < len(chart) and 0 <= nj < len(chart[0]):
            neighbors += [(ni,nj)]
    return neighbors

def get_Ns(n, chart):
    coords = []
    for i in range(len(chart)):
        for j in range(len(chart[0])):
            if chart[i][j] == n:
                coords += [(i,j)]
    return coords

chart = tuple(tuple(int(c) for c in line) for line in lines)
scores1 = [[set() for c in line] for line in chart]
scores2 = [[0 for c in line] for line in chart]
w,h = len(chart[0]), len(chart)

for n in range(9, -1, -1):
    nn_coords = get_Ns(n, chart)
    for ci, cj in nn_coords:
        if n == 9:
            scores1[ci][cj].add((ci, cj))
            scores2[ci][cj] = 1
        else:
            neighbors = get_neighbors(ci, cj, chart)
            for ni, nj in neighbors:
                neighbor = chart[ni][nj]
                if neighbor == n + 1:
                    scores1[ci][cj] = scores1[ci][cj].union(scores1[ni][nj])
                    scores2[ci][cj] += scores2[ni][nj]

total = 0
total2 = 0
for i in range(len(chart)):
    for j in range(len(chart[0])):
        if chart[i][j] == 0:
            total += len(scores1[i][j])
            total2 += scores2[i][j]

print(total)
print(total2)


end = time.perf_counter()
print(f"Execution time: {end - start:.4f} seconds")
