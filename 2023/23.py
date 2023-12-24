from collections import defaultdict
from copy import deepcopy as copy

NAMEMAP = False

def addname(xy):
    global namemap
    if xy in namemap:
        return namemap[xy]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    indx = sum(1 for k in namemap.keys() if type(k)==str)
    letter = alphabet[indx]
    assert letter not in namemap
    namemap[xy] = letter
    namemap[letter] = xy
    return letter

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

    if len(nn) == 1:
        # Initial step in the recursion
        seen.add(pos)
        lastpos,pos = pos,nn[0]
        length += 1
        nn = get_neighbors(pos)

    while len(nn) == 2:
        # Continue until we reach another node
        nextpos = nn[0] if nn[0] != lastpos else nn[1]
        pos,lastpos = nextpos,pos
        length += 1
        nn = get_neighbors(pos)

    nn_directed = get_neighbors(pos, directed)

    # We're at a node (and possibly the end of the maze) now.
    # Add positions to "seen" set and to the graph G.
    seen.add(lastpos)
    seen.add(pos)
    # start_node_nickname = addname(start_node)
    # pos_nickname = addname(pos)

    # G[start_node_nickname][pos_nickname] = length
    # if (not directed) or (lastpos == "."):
    #     G[pos_nickname][start_node_nickname] = length

    G[start_node][pos] = length
    if (not directed) or (lastpos == "."):
        G[pos][start_node] = length

    if len(nn) > 2:
        # We're at a new node. Recurse on all neighbors we haven't seen.
        for n in nn_directed:
            if n not in seen:
                traverse(start_node=pos, pos=n, directed=directed, seen=seen, G=G)

    if len(nn) == 1:
        # End of the maze. Make sure there are no dead ends.
        # assert pos == end
        pass

    return G

def longest_path_length(G, start, end, cur_node=None, visited=set(), dist_so_far=0):
    # global start, end

    if not visited:
        visited.add(cur_node)

    if cur_node == None:
        cur_node = start

    if cur_node == end:
        # print(dist_so_far, visited)
        return dist_so_far, visited

    neighbors = G[cur_node]
    maxdist = 0
    maxnodes = set()

    for node,dist in neighbors.items():
        if node not in visited:
            somedist,somenodes = longest_path_length(G, start, end, node, visited.union(set([node])), dist_so_far+dist)
            if somedist > maxdist:
                maxdist = somedist
                maxnodes = somenodes

    return maxdist,maxnodes


import time
time0 = time.time()

file = "input23.txt"
file = "test23.txt"

with open(file, 'r') as f:
    content = f.read()
    grid = [list(l) for l in content.split("\n")]

# Start and end points on the map (works for test data and input data)
start = (0,1)
end = (len(grid)-1, len(grid[0])-2)

G = traverse(start, directed=True) # part 1
# start,end = namemap[startpos],namemap[endpos]
dist,nodes = longest_path_length(G, start, end)
print(dist)

time1 = time.time()
print("%.3fs" % (time1-time0))


G = traverse(start, directed=False) # part 2
# start,end = namemap[startpos],namemap[endpos]
dist,nodes = longest_path_length(G, start, end)
print(dist)

time2 = time.time()
print("%.3fs" % (time2-time1))


# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if (i,j) in namemap and namemap[(i,j)] in nodes:
#             print("*", end="")
#         else:
#             print(grid[i][j], end="")
#     print()
