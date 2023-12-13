from collections import Counter

data = open('p14.txt', 'r').readlines()
data = [l.strip() for l in data if l.strip()]

init = data[0]
rules = [d.split(' -> ') for d in data[1:]]
poly = Counter(init[i:i+2] for i in range(len(init) - 1))

for k in range(1,41):
    new = Counter()

    for ins,out in rules:
        a = ins[0] + out
        b = out + ins[1]
        new[a] += poly[ins]
        new[b] += poly[ins]
        poly[ins] = 0

    for key in new:
        poly[key] += new[key]

    if k == 10 or k == 40:
        els = Counter()
        els[init[-1]] += 1
        for key in poly:
            els[key[0]] += poly[key]

        counts = els.values()
        print(max(counts) - min(counts))
