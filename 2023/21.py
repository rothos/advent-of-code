file = "input21.txt"
# file = "test21.txt"

with open(file, 'r') as f:
    content = f.read()
    grid = [list(l) for l in content.split("\n")]

for n in range(64):
    new_O = []
    new_dot = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                grid[i][j] = "O"

            if grid[i][j] == "O":
                for a,b in [(0,1),(0,-1),(1,0),(-1,0)]:
                        if 0<=i+a<len(grid) and 0<j+b<len(grid[0]) and grid[i+a][j+b] == ".":
                            new_O += [(i+a,j+b)]
                            new_dot += [(i,j)]

    for a,b in new_O:
        grid[a][b] = "O"

    for a,b in new_dot:
        grid[a][b] = "."


ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] in "O":
            ans += 1

# for x in grid:
#     print("".join(x))

print(ans)
