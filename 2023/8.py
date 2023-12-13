with open("input8.txt", "r") as f:
    lines = list(f.readlines())

inst = lines[0].strip()
tt = [l.strip() for l in lines[2:]]
mm = {}
for t in tt:
    a,b = t.split(' = ')
    b = b.split(', ')
    mm[a] = (b[0][1:], b[1][:-1])

inst = [0 if i == 'L' else 1 for i in inst]

cur = 'AAA'
end = 'ZZZ'
steps = 0
instindx = 0
while cur != end:
    cur = mm[cur][inst[instindx]]
    steps += 1
    instindx = (instindx+1) % len(inst)

print(steps)
