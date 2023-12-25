
import networkx as nx
import time
time0 = time.time()

file = "input25.txt"
# file = "test25.txt"

lines = open(file).read().splitlines()

G = nx.Graph()
for line in lines:
    a, bb = line.split(": ")
    bb = bb.split()

    for b in bb:
        G.add_edge(a, b, weight=1)

_, partition = nx.stoer_wagner(G)
a, b = partition
print(len(a)*len(b))

time1 = time.time()
print("%.3fs" % (time1-time0))
