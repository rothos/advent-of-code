from itertools import *

test = 0
data = open('p11%s.txt' % ('','test')[test], 'r').readlines()
data = [[int(d) for d in l.strip()] for l in data]

# part 1

def proceed(data):
    for k in range(len(data)):
        data[k] = [d+1 for d in data[k]]

    flashes = []
    flashed = True
    while flashed:
        flashed = False
        for i,j in product(range(len(data)), range(len(data[0]))):
            if data[i][j] > 9:
                flashes += [(i,j)]
                data[i][j] = -10000
                flashed = True
                for m,n in product([-1,0,1],[-1,0,1]):
                    try:
                        if i+m < 0 or j+n < 0: continue
                        data[i+m][j+n] += 1
                    except:
                        continue

    for f in flashes:
        i,j = f
        data[i][j] = 0

    return (data,len(flashes))

total = 0
dat = data.copy()
for k in range(100):
    dat,flashes = proceed(dat)
    total += flashes

print(total)


# PART 2

k = 0
dat = data.copy()
while True:
    k += 1
    dat,flashes = proceed(dat)
    if flashes == 100:
        print(k)
        break
