file = "input21.txt"
file = "input21-lawrence.txt"
# file = "test21.txt"

with open(file, 'r') as f:
    content = f.read()
    grid = [list(l) for l in content.split("\n")]

def step(grid, oo):
    oo2 = set()
    for a,b in oo:
        for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
            x = a + i
            y = b + j
            xmod = x % len(grid)
            ymod = y % len(grid[0])
            if grid[xmod][ymod] in ".S":
                oo2.add((x,y))
    return oo2

oo = set()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            oo.add((i,j))
            break

for n in range(1,5001):
    oo = step(grid, oo)
    if n % 10 == 0: print(n)
    if n in [64,65,66,131,65+131,65+131+1,65+131*2,65+131*4]:
        print(n, ":", len(oo))


# HROTHGAR
# 64 : 3716
# 65 : 3797
# 131 : 15272
# 196 : 34009
# 327 : 94353
# 589 : 305437


# LAWRENCE
# 64 : 3748
# 65 : 3787
# 66 : 4012
# 131 : 15291
# 196 : 33976
# 327 : 94315
# 589 : 305443
