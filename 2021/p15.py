from collections import Counter
from itertools import *
import astar

data = open('p15lk.txt', 'r').readlines()
matrix = [[int(d) for d in l.strip()] for l in data]

length = len(matrix)
m = [[0]*length*5 for i in range(length*5)]
for i in range(length*5):
    for j in range(length*5):
        im = i % length
        jm = j % length
        ip = i//length
        jp = j//length
        m[i][j] = (matrix[im][jm] + (ip+jp-1)) % 9 + 1

def getPathSum(adj,path):
    total = 0
    for i in range(len(path)-1):
        aa = adj[path[i]]
        for a in aa:
            if a[0] == path[i+1]:
                total += a[1]
                break
    return total

size = len(m)
adj = {}

for i in range(size):
    for j in range(size):
        key = str(i) + "," + str(j)
        if not key in adj:
            adj[key] = []
        if i+1 < size:
            adj[key] += [(str(i+1)+","+str(j), m[i+1][j])]
        if i-1 > 0:
            nk = str(i+1)+","+str(j)
            if not nk in adj:
                adj[nk] =[]
            adj[nk] += [(key, m[i][j])]
        if j+1 < size:
            adj[key] += [(str(i)+","+str(j+1), m[i][j+1])]
        if j-1 > 0:
            nk = str(i)+","+str(j+1)
            if not nk in adj:
                adj[nk] = []
            adj[nk] += [(key, m[i][j])]

start = '0,0'
end = str(size-1)+","+str(size-1)
g = astar.Graph(adj)
path = g.astar(start, end)
print(getPathSum(adj, path))

# 2851
