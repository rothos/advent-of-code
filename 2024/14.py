test = 0

if test:
    lines = open("input14test.txt", 'r').read().splitlines()
    w,h = 11,7
else:
    lines = open("input14.txt", 'r').read().splitlines()
    w,h = 101,103


import numpy as np
import re
from math import prod

t = 100
quads = [0,0,0,0]

for line in lines:
    pos, vel = [np.array(re.findall(r'-?\d+', part), dtype=int) for part in line.split()]
    x,y = ( (pos + vel*t) % [w,h] ) - np.array([w-1,h-1])//2
    if x > 0 and y > 0:
        quads[0] += 1
    elif x > 0 and y < 0:
        quads[1] += 1
    elif x < 0 and y > 0:
        quads[2] += 1
    elif x < 0 and y < 0:
        quads[3] += 1

print(prod(quads))


### PART 2

t = 0
# no tree up to 3663
while True:
    robots = set()
    for line in lines:
        pos, vel = [np.array(re.findall(r'-?\d+', part), dtype=int) for part in line.split()]
        x,y = ( (pos + vel*t) % [w,h] )
        robots.add((x,y))
    for i in range(h):
        line = ""
        for j in range(w):
            line += 'X' if (j,i) in robots else '.'
        print(line)
    _ = input(f'^ t = {t}')
    t += 1
