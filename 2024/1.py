file = "input1.txt"
# file = "input1test.txt"


### PART 1

with open(file, 'r') as f:
    lines = f.readlines()

aa = []
bb = []
for line in lines:
    aa += [int(line.split(' ')[0])]
    bb += [int(line.split(' ')[-1])]

aa = sorted(aa)
bb = sorted(bb)
total = sum(abs(aa[i]-bb[i]) for i in range(len(aa)))
print(total)


### PART 2

total = 0
for a in aa:
    total += a*sum(1 for b in bb if b == a)

print(total)
