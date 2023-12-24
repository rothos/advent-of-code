from collections import defaultdict
from copy import deepcopy as copy

# RUNNING PART 1 AND PART 2 IN SUCCESSION HERE DOESN'T WORK
# I REALLY DON'T KNOW WHY
# :(((

def get_neighbors(pt, directed=False):
    # Returns the indices of valid neighbors
    global grid
    r,c = pt
    neighbors = []
    for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
        if 0<=r+i<len(grid) and 0<=c+j<len(grid[0]):
            tile = grid[r+i][c+j]
            if directed:
                if tile == "." \
                    or (tile == "<" and j == -1) \
                    or (tile == ">" and j == 1) \
                    or (tile == "^" and i == -1) \
                    or (tile == "v" and i == 1):
                        neighbors.append((r+i, c+j))
            elif tile != "#":
                neighbors.append((r+i, c+j))

    return neighbors

def traverse(start_node, pos=None, directed=True, seen=set(), G=defaultdict(dict)):
    length = 1
    lastpos = start_node
    if not pos: 
        pos = start_node
        length = 0 # We don't count the initial starting point as a step
    else:
        seen.add(pos)

    nn = get_neighbors(pos, directed)

    # Initial step in the recursion
    if len(nn) == 1:
        seen.add(pos)
        lastpos,pos = pos,nn[0]
        length += 1
        nn = get_neighbors(pos)

    # Continue until we reach another node
    while len(nn) == 2:
        nextpos = nn[0] if nn[0] != lastpos else nn[1]
        pos,lastpos = nextpos,pos
        length += 1
        nn = get_neighbors(pos)

    nn_directed = get_neighbors(pos, directed)

    # We're at a node (and possibly the end of the maze) now.
    # Add positions to "seen" set and to the graph G.
    seen.add(lastpos)
    seen.add(pos)
    G[start_node][pos] = length
    if (not directed) or (lastpos == "."):
        G[pos][start_node] = length

    # If we're at a new node, recurse on all neighbors we haven't seen.
    if len(nn) > 2:
        for n in nn_directed:
            if n not in seen:
                G = traverse(start_node=pos, pos=n, directed=directed, seen=seen, G=G)

    return G

def longest_path_length(G, start, end, cur_node=None, visited=set(), dist_so_far=0):
    if cur_node == None:
        cur_node = start

    if not visited:
        visited.add(cur_node)

    if cur_node == end:
        return dist_so_far, visited

    neighbors = G[cur_node]
    maxdist = 0
    maxnodes = set()

    for node,dist in neighbors.items():
        if node not in visited:
            somedist,somenodes = longest_path_length(G, start, end, node,
                                    visited.union(set([node])), dist_so_far+dist)
            if somedist > maxdist:
                maxdist = somedist
                maxnodes = somenodes

    return maxdist,maxnodes


import time
time0 = time.time()

file = "input23.txt"
# file = "test23.txt"

with open(file, 'r') as f:
    content = f.read()
    grid = [list(l) for l in content.split("\n")]


# Start and end points on the map (works for test data and input data)
start = (0,1)
end = (len(grid)-1, len(grid[0])-2)


# Part 1 or part 2
part_1 = True

G = traverse(start, directed=part_1)
dist,nodes = longest_path_length(G, start, end)
print(dist)

time1 = time.time()
print("%.3fs" % (time1-time0))
