import copy

import time
time0 = time.time()

# file = "input22-lawrence.txt"
file = "input22.txt"
# file = "test22.txt"

with open(file, 'r') as f:
    content = f.read()
    lines = [l for l in content.split("\n")]

_n = 0

class brick:
    def __init__(self, xyz0, xyz1):
        global _n
        self.xyz0 = xyz0
        self.xyz1 = xyz1
        # self.id = chr(_n+65)
        self.id = _n
        _n += 1

    def shift(self, x, y, z):
        self.xyz0 = [x+self.xyz0[0], y+self.xyz0[1], z+self.xyz0[2]]
        self.xyz1 = [x+self.xyz1[0], y+self.xyz1[1], z+self.xyz1[2]]

    def __repr__(self):
        return str(self.xyz0) + "," + str(self.xyz1)

bricks = []

for line in lines:
    a,b = line.split("~")
    a = [int(x) for x in a.split(",")]
    b = [int(x) for x in b.split(",")]
    bricks.append(brick(a,b))

bricks = sorted(bricks, key=lambda b: b.xyz0[2])

# Drop the bricks
for i,brick in enumerate(bricks):
    x0,y0,z0 = brick.xyz0
    x1,y1,z1 = brick.xyz1

    maxz = 0
    for under in bricks[:i]:
        ux0,uy0,uz0 = under.xyz0
        ux1,uy1,uz1 = under.xyz1

        if not ((ux1 < x0 or x1 < ux0) or (uy1 < y0 or y1 < uy0)):
            maxz = max(maxz, uz1)

    brick.shift(0,0,-z0+maxz+1)

G = dict()
for brick in bricks:
    G[brick.id] = {"supports": [], "supported_by": []}

# Check which bricks support others
for i,brick in enumerate(bricks):
    x0,y0,z0 = brick.xyz0
    x1,y1,z1 = brick.xyz1

    for under in bricks[:i]:
        ux0,uy0,uz0 = under.xyz0
        ux1,uy1,uz1 = under.xyz1

        if uz1 + 1 == z0 and not ((ux1 < x0 or x1 < ux0) or (uy1 < y0 or y1 < uy0)):
            G[brick.id]["supported_by"].append(under.id)
            G[under.id]["supports"].append(brick.id)

names = set()

for name, info in G.items():
    # We are interested in bricks that can be disintegrated
    # I.e. bricks whose "supports" are bricks that have at least two "supported bys"

    for over in info["supports"]:
        if len(G[over]["supported_by"]) < 2:
            break
    else:
        names.add(name)

print(len(names))

time1 = time.time()
print("-- %.3fs --" % (time1-time0))
# 475


# ----------------------------------------------------------------------

ans = 0

for i in range(len(bricks)):
    destroyed = bricks[i]
    if destroyed.id in names:
        continue

    BRICKS = copy.deepcopy(bricks)
    BRICKS.pop(i)

    # Drop the bricks
    for i,brick in enumerate(BRICKS):
        x0,y0,z0 = brick.xyz0
        x1,y1,z1 = brick.xyz1

        maxz = 0
        for under in BRICKS[:i]:
            ux0,uy0,uz0 = under.xyz0
            ux1,uy1,uz1 = under.xyz1

            if not ((ux1 < x0 or x1 < ux0) or (uy1 < y0 or y1 < uy0)):
                maxz = max(maxz, uz1)

        brick.shift(0,0,-z0+maxz+1)
        if -z0+maxz+1 != 0:
            ans += 1

print(ans)

time2 = time.time()
print("-- %.3fs --" % (time2-time1))
# 79144
# -- 370.935s --
