from itertools import combinations
import numpy as np
import random
random.seed(0)

import time
time0 = time.time()

file = "input24.txt"
# file = "test24.txt"

with open(file, 'r') as f:
    content = f.read()
    lines = [l for l in content.split("\n")]

class particle():
    def __init__(self,pos,vel):
        self.pos = [int(n) for n in pos]
        self.vel = [int(n) for n in vel]
    def __repr__(self):
        return str([self.pos, self.vel])

def calc_intersection_xy(a,b):
    MIN = 200000000000000
    MAX = 400000000000000
    # MIN = 7
    # MAX = 27

    apx, apy, apz = a.pos
    avx, avy, avz = a.vel
    bpx, bpy, bpz = b.pos
    bvx, bvy, bvz = b.vel

    denom = (avy - bvy*avx/bvx)
    if denom == 0:
        # The lines are parallel
        return False

    t1 = (bpy + bvy/bvx*(apx-bpx) - apy) / denom
    t2 = (apx + avx*t1 - bpx)/bvx

    if t1 < 0 or t2 < 0:
        # They intersected in the past
        return False

    xi = apx + t1*avx
    yi = apy + t1*avy

    if (MIN <= xi <= MAX) and (MIN <= yi <= MAX):
        # They intersect in the zone!
        return True
    else:
        # They intersect outside the zone
        return False

pp = []
for line in lines:
    pos,vel = line.split("@")
    pp.append(particle(pos.split(","), vel.split(",")))

total = sum(calc_intersection_xy(a,b) for a,b in combinations(pp,2))
print(total)

time1 = time.time()
print("%.3fs" % (time1-time0))



# PART 2

a,b,c = pp[0],pp[1],pp[-1]
pax,pay,paz = a.pos
vax,vay,vaz = a.vel
pbx,pby,pbz = b.pos
vbx,vby,vbz = b.vel
pcx,pcy,pcz = c.pos
vcx,vcy,vcz = c.vel

def J(x):
    px,vx,py,vy,pz,vz,ta,tb,tc = x
    return np.array([
            [1, ta, 0, 0, 0, 0, vx-vax, 0, 0],
            [0, 0, 1, ta, 0, 0, vy-vay, 0, 0],
            [0, 0, 0, 0, 1, ta, vz-vaz, 0, 0],
            [1, tb, 0, 0, 0, 0, 0, vx-vbx, 0],
            [0, 0, 1, tb, 0, 0, 0, vy-vby, 0],
            [0, 0, 0, 0, 1, tb, 0, vz-vbz, 0],
            [1, tc, 0, 0, 0, 0, 0, 0, vx-vcx],
            [0, 0, 1, tc, 0, 0, 0, 0, vy-vcy],
            [0, 0, 0, 0, 1, tc, 0, 0, vz-vcz]
        ])

def f(x):
    px,vx,py,vy,pz,vz,ta,tb,tc = x
    return np.array([
            px + vx*ta - pax - vax*ta,
            py + vy*ta - pay - vay*ta,
            pz + vz*ta - paz - vaz*ta,
            px + vx*tb - pbx - vbx*tb,
            py + vy*tb - pby - vby*tb,
            pz + vz*tb - pbz - vbz*tb,
            px + vx*tc - pcx - vcx*tc,
            py + vy*tc - pcy - vcy*tc,
            pz + vz*tc - pcz - vcz*tc,
        ])

x0 = np.array([random.random() for i in range(9)])

# Iterate with Newton's method
for step in range(50):
    x0 += np.linalg.solve(J(x0), -f(x0))

print(x0[0] + x0[2] + x0[4])

time2 = time.time()
print("%.3fs" % (time2-time1))
