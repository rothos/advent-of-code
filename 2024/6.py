lines = open("input6.txt", 'r').read().splitlines()
# lines = open("input6test.txt", 'r').read().splitlines()

lines = [list(l) for l in lines]


### PART 1

def rotate(direction):
    if direction == (-1,0): return (0,1)
    if direction == (0,1): return (1,0)
    if direction == (1,0): return (0,-1)
    if direction == (0,-1): return (-1,0)
    return None

visited = set()

gi = None
for i,line in enumerate(lines):
    if "^" in line:
        gi = i
        gj = j = line.index("^")
        break

i,j = gi,gj

visited.add((i,j))

direction = (-1,0)
while 0 <= i+direction[0] < len(lines[0]) and 0 <= j+direction[1] < len(lines):
    i2, j2 = i+direction[0], j+direction[1]
    if lines[i2][j2] == "#":
        direction = rotate(direction)
    else:
        i,j = i2,j2
        visited.add((i,j))

print(len(visited))


### PART 2

obstructions = set()
for x,y in visited:
    obstructions.add((x,y))
    if 0<=x+1<len(lines[0]): obstructions.add((x+1,y))
    if 0<=x-1<len(lines[0]): obstructions.add((x-1,y))
    if 0<=y+1<len(lines): obstructions.add((x,y+1))
    if 0<=y-1<len(lines): obstructions.add((x,y-1))

if (gi,gj) in obstructions:
    obstructions.remove((gi,gj))

count = 0

for ob in obstructions:
    visited = set()
    i,j = gi,gj
    direction = (-1,0)
    visited.add((i,j,direction))

    while 0 <= i+direction[0] < len(lines[0]) and 0 <= j+direction[1] < len(lines):
        i2, j2 = i+direction[0], j+direction[1]
        
        if lines[i2][j2] == "#" or (i2,j2) == ob:
            direction = rotate(direction)
        else:
            i,j = i2,j2

        if (i,j,direction) in visited:
            count += 1
            break

        visited.add((i,j,direction))

print(count)
