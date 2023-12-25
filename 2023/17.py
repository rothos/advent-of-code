import heapq
def shortest_path(start, is_end, neighbors_function):
    seen = set()
    queue = [(0, (start, [start]))]
    while queue:
        cost, (node, path) = heapq.heappop(queue)
        if node not in seen:
            seen.add(node)
            if is_end(node):
                return path,cost
            for neighbor,thiscost in neighbors_function(node):
                heapq.heappush(queue, (cost + thiscost, (neighbor, path + [neighbor])))


def neighbors(node):
    (x,y),(dx,dy),streak = node
    nn = []
    for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
        if (0<=(x+i)<len(grid)) and (0<=(y+j)<len(grid[0])) and (i!=-dx or j!=-dy):
            coords = (x+i,y+j)
            direction = (i,j)
            cost = int(grid[x+i][y+j])
            if (i,j) != (dx,dy):
                nn += [((coords,direction,1),cost)]
            elif streak+1 <= 3:
                nn += [((coords,direction,streak+1),cost)]
    return nn


def neighbors2(node):
    (x,y),(dx,dy),streak = node
    nn = []
    for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
        if (0<=(x+i)<len(grid)) and (0<=(y+j)<len(grid[0])) and (i!=-dx or j!=-dy):
            coords = (x+i,y+j)
            direction = (i,j)
            cost = int(grid[x+i][y+j])
            if (i,j) != (dx,dy) and 4<=streak<=10:
                nn += [((coords,direction,1),cost)]
            elif (i,j) == (dx,dy) and streak < 10:
                nn += [((coords,direction,streak+1),cost)]
    return nn


def is_end(node):
    return node[0] == (len(grid)-1, len(grid[0])-1)


import time
time0 = time.time()

file = "input17.txt"
# file = "test17.txt"


with open(file, 'r') as f:
    content = f.read()
    grid = content.split("\n")


start = ((0,0),(0,0),10)

path,cost = shortest_path(start, is_end, neighbors)
print(cost)


# Lawrence pointed out that this shouldn't work, but it does.
# My code doesn't account for the fact that there needs to be
# a streak of at least 4 at the very end; I just got lucky.
path,cost = shortest_path(start, is_end, neighbors2)
print(cost)


# steps = [p[0] for p in path]
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if (i,j) in steps:
#             print(".", end="")
#         else:
#             print(grid[i][j], end="")
#     print()

time1 = time.time()
print("%.3fms" % (time1-time0))
