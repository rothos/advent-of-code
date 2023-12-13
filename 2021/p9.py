from itertools import permutations

test = 0
data = open('p9%s.txt' % ('','test')[test], 'r').readlines()
data = [[int(d) for d in l.strip()] for l in data]

# Part 1

aa = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if  (i-1 < 0             or data[i][j] < data[i-1][j])  \
        and (i+1 >= len(data)    or data[i][j] < data[i+1][j])  \
        and (j-1 < 0             or data[i][j] < data[i][j-1])  \
        and (j+1 >= len(data[0]) or data[i][j] < data[i][j+1]):

            aa += [data[i][j]]

print(aa,sum(a+1 for a in aa))


# Part 2

def prod(l):
    return reduce(lambda x,y: x*y, l, 1)

def go_down(i,j):
    if i>0 and data[i-1][j] < data[i][j]:
        return (i-1,j)
    if i+1<len(data) and data[i+1][j] < data[i][j]:
        return (i+1,j)
    if j>0 and data[i][j-1] < data[i][j]:
        return (i,j-1)
    if j+1<len(data[0]) and data[i][j+1] < data[i][j]:
        return (i,j+1)
    return (i,j)

def find_basin(i,j):
    while go_down(i,j) != (i,j):
        i,j = go_down(i,j)
    return str(i) + "," + str(j)

basins = {}
for i in range(len(data)):
    for j in range(len(data[0])):
        basins[str(i) + "," + str(j)] = 0

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 9:
            continue
        basins[find_basin(i,j)] += 1

sizes = sorted([basins[k] for k in basins])
print(prod(sizes[-3:]))
