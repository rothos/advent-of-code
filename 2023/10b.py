file = "input10.txt"
# file = "test10b.txt"

with open(file, 'r') as f:
    lines = list([l.strip() for l in f.readlines()])

x = -1
for y,l in enumerate(lines):
    if 'S' in l:
        x = l.index('S')
        break

xy = [(x,y)]

direction = 's'
steps = 0
tile = '|'
while tile != 'S':
    if direction == 'n': y -= 1
    if direction == 's': y += 1
    if direction == 'w': x -= 1
    if direction == 'e': x += 1
    steps += 1
    tile = lines[y][x]
    xy += [(x,y)]
    if tile == 'L' and direction == 's': direction = 'e'
    if tile == 'L' and direction == 'w': direction = 'n'
    if tile == 'F' and direction == 'n': direction = 'e'
    if tile == 'F' and direction == 'w': direction = 's'
    if tile == '7' and direction == 'e': direction = 's'
    if tile == '7' and direction == 'n': direction = 'w'
    if tile == 'J' and direction == 'e': direction = 'n'
    if tile == 'J' and direction == 's': direction = 'w'

del xy[-1]

ins = []
for y in range(len(lines)):
    IN = False
    direction = None
    for x in range(len(lines[0])):
        if (x,y) in xy:
            tile = lines[y][x]
            if tile == "|":
                IN = not IN
            if tile == "F":
                direction = "down"
            if tile == "L":
                direction = "up"
            if tile == "J" and direction == "down":
                IN = not IN
            if tile == "7" and direction == "up":
                IN = not IN
        elif IN:
            ins += [(x,y)]

print(len(ins))
# print(ins)
