file = "input11.txt"
# file = "test11.txt"

import re

with open(file, 'r') as f:
    universe = list([l.strip() for l in f.readlines()])

def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def empty_xy(universe):
    xx,yy = [],[]

    for y,sector in enumerate(universe):
        if not '#' in sector:
            yy += [y]

    for x,sector in enumerate(transpose(universe)):
        if not '#' in sector:
            xx += [x]

    return xx,yy

def get_galaxy_coords(universe):
    cc = []
    for y,sector in enumerate(universe):
        cc += [(x,y) for x,tile in enumerate(sector) if tile=='#']
    return cc

def count_paths(universe, expansion_factor):
    gxy = get_galaxy_coords(universe)
    exx,eyy = empty_xy(universe)

    total = 0
    for i in range(len(gxy)):
        for j in range(i+1,len(gxy)):
            a,b = gxy[i],gxy[j]

            xdist = abs(a[0]-b[0]) + (expansion_factor-1)*sum(map(lambda x: min(a[0],b[0]) < x < max(a[0],b[0]), exx))
            ydist = abs(a[1]-b[1]) + (expansion_factor-1)*sum(map(lambda x: min(a[1],b[1]) < x < max(a[1],b[1]), eyy))

            total += xdist + ydist

    return total

print(count_paths(universe,2))
print(count_paths(universe,1000000))
