lines = open("input10.txt", 'r').read().splitlines()
# lines = open("input10test.txt", 'r').read().splitlines()

chart = tuple(tuple(int(c) for c in line) for line in lines)
w, h = len(chart[0]), len(chart)

def solve():
    scores1 = [[set() for _ in line] for line in chart]
    scores2 = [[0 for _ in line] for line in chart]
    
    for n in range(9, -1, -1):
        for ci in range(h):
            for cj in range(w):
                if chart[ci][cj] != n: continue
                if n == 9:
                    scores1[ci][cj].add((ci, cj))
                    scores2[ci][cj] = 1
                else:
                    for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                        ni, nj = ci+di, cj+dj
                        if 0 <= ni < h and 0 <= nj < w and chart[ni][nj] == n+1:
                            scores1[ci][cj] |= scores1[ni][nj]
                            scores2[ci][cj] += scores2[ni][nj]
    
    return sum(len(scores1[i][j]) for i in range(h) for j in range(w) if chart[i][j] == 0), \
           sum(scores2[i][j] for i in range(h) for j in range(w) if chart[i][j] == 0)

import time
start = time.perf_counter()
print(*solve())
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
