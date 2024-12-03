file = "input1.txt"
# file = "input1test.txt"

lines = open(file, 'r').read().splitlines()


### PART 1

aa,bb = zip(*[tuple(l.split('   ')) for l in lines])
aa,bb = sorted(int(a) for a in aa), sorted(int(b) for b in bb)
total = sum(abs(aa[i]-bb[i]) for i in range(len(aa)))
print(total)


### PART 2

print( sum(a*sum(1 for b in bb if b == a) for a in aa) )
