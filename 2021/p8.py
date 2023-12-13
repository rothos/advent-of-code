from itertools import permutations

test = 0
data = open('p8%s.txt' % ('','test')[test], 'r').readlines()
data = map(lambda l: [p.strip().split() for p in l.split('|')], data)

# Part 1

x = 0
for d in data:
    for k in d[1]:
        if len(k) in [2,3,4,7]:
            x += 1
print(x)


# Part 2

ref = ['abcefg','cf','acdeg','acdfg',
       'bcdf','abdfg','abdefg','acf',
       'abcdefg','abcdfg']

getsig = lambda ins: tuple(sorted([len(q) for q in ins if a in q]))

master = {}
for a in 'abcdefg':
    master[getsig(ref)] = a

total = 0
for line in data:
    inputs = line[0]
    outputs = line[1]

    mapping = {}
    for a in 'abcdefg':
        mapping[a] = master[getsig(inputs)]

    num = 0
    for digit in outputs:
        digit = "".join(sorted([mapping[d] for d in digit]))
        num = num*10 + ref.index(digit)

    total += num

print(total)
