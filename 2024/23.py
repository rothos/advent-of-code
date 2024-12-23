text = open("input23.txt", 'r').read().splitlines()
# text = open("input23test.txt", 'r').read().splitlines()

import networkx as nx
import time
start = time.perf_counter()

# Build the graph
G = nx.Graph()
for line in text:
    a, b = line.split('-')
    G.add_edge(a, b)

cliques = nx.enumerate_all_cliques(G)
biggest_clique = None
num_triangles_with_a_t_node = 0
for clique in cliques:
    biggest_clique = clique
    if len(clique) == 3 and any(node[0] == 't' for node in clique):
        num_triangles_with_a_t_node += 1

print(num_triangles_with_a_t_node)
print(",".join(sorted(biggest_clique)))

print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
