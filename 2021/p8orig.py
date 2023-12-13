from itertools import permutations

test = 0
data = open('p8%s.txt' % ('','test')[test], 'r').readlines()
data = map(lambda l: [p.split() for p in l.strip().split(' | ')], data)

# Part 1

x = 0
for d in data:
    for k in d[1]:
        if len(k) in [2,3,4,7]:
            x += 1
print(x)


# Part 2

pp = [2,3,5,7,11,13,17]
aa = 'abcdefg'
key = ['abcefg','cf','acdeg','acdfg',
       'bcdf','abdfg','abdefg','acf',
       'abcdefg','abcdfg']

# Product of list
def prod(l):
    return reduce(lambda x,y: x*y, l, 1)

# Functions for verifying whether a particular mapping is correct
chr2pp = lambda c,cmap: pp[ord(cmap[ord(c)-97])-97]
txt2num = lambda t,cmap: prod([chr2pp(i,cmap) for i in t])
getTotal = lambda a,cmap: sum([txt2num(q,cmap) for q in a])

# Reference value for correct mapping
reference = getTotal(key,aa)
keysums = [txt2num(i,aa) for i in key]

total = 0
for line in data:
    perms = permutations(aa)
    # Search for the correct permutation
    for perm in perms:
        if getTotal(line[0],perm) == reference:
            # We found the key, now simply decode
            digits = []
            for code in line[1]:
                codetotal = txt2num(code,perm)
                # Lazy loop to return the correct digit
                for i in range(10):
                    if codetotal == keysums[i]:
                        digits += [i]
                        break

            # Join the digits into a 4-digit number, add to total
            num = int("".join(str(d) for d in digits))
            total += num
            break

print(total)
