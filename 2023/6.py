from math import floor,ceil,prod
with open("input6.txt", "r") as f:
    lines = list(f.readlines())

def bloop(t,d):
    return 1 + floor(-10e-15+(t+(t*t-4*d)**.5)/2) - ceil(10e-15+(t-(t*t-4*d)**.5)/2)

tt,dd = [list(map(int, filter(any, l.split(":")[1].split(" ")))) for l in lines]
print(prod(bloop(tt[i],dd[i]) for i in range(len(tt))))

t,d = [int(l.split(":")[1].replace(" ","")) for l in lines]
print(bloop(t,d))


