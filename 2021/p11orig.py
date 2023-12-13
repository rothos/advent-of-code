from itertools import *
from more_itertools import *

test = 0
data = open('p11%s.txt' % ('','test')[test], 'r').readlines()
data = [[int(d) for d in l.strip()] for l in data]

# part 1

def add1(data,i,j):
    data = [[0]+d+[0] for d in data]
    data = [[0]*len(data[0])] + data + [[0]*len(data[0])]
    for a in range(3):
        for b in range(3):
            if a == 1 and b == 1:
                continue
            data[i+a][j+b] += 1
    data = [d[1:-1] for d in data]
    return data[1:-1]

def proceed(data):
    for k in range(len(data)):
        data[k] = [d+1 for d in data[k]]

    flashes = []
    thing = True
    while thing:
        thing = False
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] > 9:
                    flashes += [(i,j)]
                    data = add1(data,i,j)
                    data[i][j] = -1000
                    thing = True

    for f in flashes:
        data[f[0]][f[1]] = 0

    return (data,len(flashes))

def printy(data):
    for d in data:
        print("".join([str(c) for c in d]))

total = 0
for k in range(100):
    data,flashes = proceed(data)
    total += flashes

print(total)




# PART 2



def proceed2(data):
    for k in range(len(data)):
        data[k] = [d+1 for d in data[k]]

    flashes = []
    thing = True
    while thing:
        thing = False
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] > 9:
                    flashes += [(i,j)]
                    data = add1(data,i,j)
                    data[i][j] = -1000
                    thing = True

    for f in flashes:
        data[f[0]][f[1]] = 0

    return (data,len(flashes))

k = 0
flag = True
while flag:
    k += 1
    data,flashes = proceed2(data)
    if flashes == 100:
        print(100+k)
        break
