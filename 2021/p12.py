data = open('p12.txt', 'r').readlines()
data = [l.strip().split('-') for l in data]

network = {}
for d in data:
    a,b = d
    if a not in network: network[a] = []
    if b not in network: network[b] = []
    network[a] += [b]
    network[b] += [a]

def findpaths(network, path=['start'], allowdouble=False):
    paths = []
    for p in network[path[-1]]:
        if p == 'start':
            continue

        if p == 'end':
            paths += [path + [p]]
            continue

        lowers = [q for q in path if q == q.lower()]
        if p == p.lower() and p in path and (not allowdouble or len(lowers) != len(set(lowers))):
            continue

        paths += findpaths(network, path + [p], allowdouble)

    return paths

# part 1
print(len(findpaths(network)))

# part 2
print(len(findpaths(network, allowdouble=True)))
