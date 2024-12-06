lines = open("input6.txt", 'r').read().splitlines()
lines = open("input6test.txt", 'r').read().splitlines()

lines = [list(l) for l in lines]


### PART 1

# The guard rotates clockwise at any obstruction
def rotate(direction):
    if direction == (-1,0): return (0,1)
    if direction == (0,1): return (1,0)
    if direction == (1,0): return (0,-1)
    if direction == (0,-1): return (-1,0)
    return None

# Locate the guard, call its starting coords (gi,gj)
gi = None
for i,line in enumerate(lines):
    if "^" in line:
        gi = i
        gj = j = line.index("^")
        break

# i,j are current guard coordinates
i,j = gi,gj
visited = set()
visited.add((i,j))

# Traverse the map
direction = (-1,0)
while 0 <= i+direction[0] < len(lines[0]) and 0 <= j+direction[1] < len(lines):
    i2, j2 = i+direction[0], j+direction[1]
    # Rotate if we've hit an obstruction
    if lines[i2][j2] == "#":
        direction = rotate(direction)
    else:
        # Proceed forward
        i,j = i2,j2
        visited.add((i,j))

# The answer is how many cells the guard has visited
print(len(visited))


### PART 2

# All candidate obstructions must be adjacent to a cell that the
# guard has already traversed.
obstructions = set()
for x,y in visited:
    obstructions.add((x,y))
    if 0<=x+1<len(lines[0]): obstructions.add((x+1,y))
    if 0<=x-1<len(lines[0]): obstructions.add((x-1,y))
    if 0<=y+1<len(lines): obstructions.add((x,y+1))
    if 0<=y-1<len(lines): obstructions.add((x,y-1))

# We can't place an obstruction in the place the guard started
obstructions.remove((gi,gj))

# We're counting how many new obstructions lead to cycles
count = 0
for ob in obstructions:

    # Reset variables for this traversal
    visited = set()
    i,j = gi,gj
    direction = (-1,0)
    visited.add((i,j,direction))

    # Traverse the map
    while 0 <= i+direction[0] < len(lines[0]) and 0 <= j+direction[1] < len(lines):
        i2, j2 = i+direction[0], j+direction[1]
        
        # We treat `ob` as an obstruction
        if lines[i2][j2] == "#" or (i2,j2) == ob:
            direction = rotate(direction)
        else:
            i,j = i2,j2

        # Increment counter and break if we've hit a cycle
        if (i,j,direction) in visited:
            count += 1
            break

        visited.add((i,j,direction))

print(count)
