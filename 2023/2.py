from math import prod

file = "input2.txt"
# file = "test2.txt"

### PART 1

with open(file, 'r') as f:
    lines = f.readlines()

def strips(l):
    return [x.strip() for x in l]

def parsegrab(grab):
    parts = strips(grab.split(','))
    out = {'red': 0, 'green': 0, 'blue': 0}
    for part in parts:
        x = part.split(' ')
        num = int(x[0])
        color = x[1]
        out[color] = num
    return out

def checkgrab(grab, bag):
    if grab['red'] > bag['red'] or \
            grab['green'] > bag['green'] or \
            grab['blue'] > bag['blue']:
        return False
    else:
        return True

def parseline(line):
    colonsplit = strips(line.split(': '))
    gid = int(colonsplit[0].split(' ')[1])
    grabtxt = strips(colonsplit[1].split(';'))
    grabs = [parsegrab(grab) for grab in grabtxt]
    return gid, grabs

def countgame(line, bag):
    gid, grabs = parseline(line)
    valids = [checkgrab(grab, bag) for grab in grabs]
    return gid, all(valids)

bag = {'red': 12, 'green': 13, 'blue': 14}
total = 0

for line in lines:
    gid, valid = countgame(line, bag)
    if valid:
        total += gid

print(total)
# 2061


### PART 2

def mincolors(grabs):
    out = {'red': 0, 'green': 0, 'blue': 0}
    for grab in grabs:
        out['red'] = max(out['red'], grab['red'])
        out['green'] = max(out['green'], grab['green'])
        out['blue'] = max(out['blue'], grab['blue'])
    return out

def getpower(line):
    gid, grabs = parseline(line)
    mins = mincolors(grabs)
    power = mins['red'] * mins['green'] * mins['blue']
    return power

total2 = 0

for line in lines:
    total2 += getpower(line)

print(total2)