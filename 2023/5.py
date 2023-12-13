file = "input5.txt"
# file = "test5.txt"

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

### PART 1

with open(file, 'r') as f:
    content = f.read()

blocks = [x.split(" map:") for x in content.split("\n\n")]
seeds = [int(x) for x in blocks[0][0].split(": ")[1].split(" ")]
tmaps = [x[1].strip().split("\n") for x in blocks[1:]]
maps = []

for t in tmaps:
    mappo = []
    for l in t:
        m = dotdict(dict())
        nn = [int(x) for x in l.split(" ")]
        m.dest = nn[0]
        m.source = nn[1]
        m.range = nn[2]
        mappo += [m]
    maps += [mappo]

outs = []

for seed in seeds:
    # print(seed)
    for mm in maps:
        for r in mm:
            if seed >= r.source and seed < r.source + r.range:
                # print(seed, r, seed - r.source + r.dest)
                seed = seed - r.source + r.dest
                break
    outs += [seed]
    # print()

print(min(outs))
# 84470622
