file = "input5.txt"
# file = "test5.txt"

from functools import reduce

with open(file, 'r') as f:
    content = f.read()

class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

blocks = [x.split(" map:") for x in content.split("\n\n")]
seeds = [int(x) for x in blocks[0][0].split(": ")[1].split(" ")]
tmaps = [x[1].strip().split("\n") for x in blocks[1:]]
maps = []

seeds = [(seeds[i],seeds[i]+seeds[i+1]) for i in range(0, len(seeds)//2+1, 2)]

for t in tmaps:
    maplines = []
    for l in t:
        m = dotdict(dict())
        m.dest, m.source, m.range = [int(x) for x in l.split(" ")]
        m.in0 = m.source
        m.in1 = m.source+m.range
        m.out0 = m.dest
        m.out1 = m.dest+m.range
        maplines += [m]
    maps += [maplines]


def split_at(seedranges, point):
    newranges = []

    for seedrange in seedranges:
        s0,s1 = seedrange
        if s0 < point < s1:
            newranges += [(s0, point)]
            newranges += [(point, s1)]
        else:
            newranges += [seedrange]

    return newranges

def splitranges(seedranges, mapp):

    splitpoints = []
    for m in mapp:
        splitpoints += [m.in0, m.in1]

    for point in splitpoints:
        seedranges = split_at(seedranges, point)

    return seedranges


def map_it(seed, m):
    if not m.source <= seed < m.source+m.range:
        print('ERROR1',seed,m)
    return seed - m.source + m.dest

def maprange(seedrange, m):
    s0, s1 = seedrange
    s1 = s1-1

    m0 = m.source
    m1 = m.source + m.range - 1

    if s1 < m0 or s0 > m1:
        return [(s0,s1)]

    if s0 >= m0 and s1 <= m1:
        # print('case 1')
        return [(map_it(s0,m), map_it(s1,m))]

    if s0 < m0 and s1 <= m1:
        # print('case 2')
        return [
            (s0, m0-1),
            (map_it(m0,m), map_it(s1,m))
        ]

    if s0 >= m0 and s1 > m1:
        # print('case 3')
        return [
            (map_it(s0,m), map_it(m1,m)),
            (m1+1, s1)
        ]

    if s0 < m0 and s1 > m1:
        # print('case 4')
        return [
            (s0, m0-1),
            (map_it(m0,m), map_it(m1,m)),
            (m1+1, s1)
        ]

    print("ERROR2", (s0,s1), m)

mapped = []

for seed in seeds:
    seedranges = [seed]
    for mapp in maps:
        # print("seedranges:",seedranges)
        seedranges = splitranges(seedranges, mapp)
        # print("splitranges:",seedranges)
        newranges = []
        for seedrange in seedranges:
            in_map = 0
            for m in mapp:
                s0,s1 = seedrange
                if (s0 >= m.in0 and s1 <= m.in1):
                    # print("mapping range:", seedrange, m)
                    newranges += maprange(seedrange, m)
                    in_map = 1
                    break
                # elif (s1 <= m.in0) or (s0 >= m.in1):
                #     newranges += [seedrange]
                # else:
                    print("ERROR3", s0, s1, m)
            if not in_map:
                newranges += [seedrange]

        seedranges = list(set(newranges))

    mapped += seedranges

# print(mapped)

# seeds = [(20,30),(30,60),(97,101)]
# print(splitranges(seeds,maps[0]))

# print(map_it(45, maps[0][1]))

print(reduce(lambda x,y: min(x,y[0]), mapped, mapped[0][0]))
