data = open('p13.txt', 'r').readlines()
data = [l.strip() for l in data if l.strip()]

folds = []
coords = []
for l in data:
    if l[0] == 'f':
        a,b = l.split('=')
        folds.append((a[-1],int(b)))
    else:
        coords.append(tuple([int(t) for t in l.split(',')]))

for k,fold in enumerate(folds):
    axis,z = fold
    for i,coord in enumerate(coords):
        x,y = coord
        if axis == 'x' and x > z:
            x = 2*z - x
        elif axis == 'y' and y > z:
            y = 2*z - y
        coords[i] = (x,y)

    coords = list(set(coords))
    if k == 0:
        print(len(coords)) # 810

X = max(c[0] for c in coords)
Y = max(c[1] for c in coords)

for y in range(Y+1):
    s = ''
    for x in range(X+1):
        if (x,y) in coords:
            s += '#'
        else:
            s += '.'
    print(s)

#..#.#....###..#..#.###...##..####.###.
#..#.#....#..#.#..#.#..#.#..#.#....#..#
####.#....###..#..#.###..#....###..#..#
#..#.#....#..#.#..#.#..#.#.##.#....###.
#..#.#....#..#.#..#.#..#.#..#.#....#.#.
#..#.####.###...##..###...###.#....#..#
