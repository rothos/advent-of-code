
# part 1

hh = open('p2a.txt','r').readlines()
vv = open('p2b.txt','r').readlines()
hh = map(int, hh)
vv = map(int, vv)

print(sum(hh)*sum(vv))


# part 2

ff = open('p2.txt','r').readlines()
aim = 0
hpos = 0
dpos = 0
for f in ff:
	n = int(f.split()[1])
	if f[0] == 'd':
		aim += n
	if f[0] == 'u':
		aim -= n
	if f[0] == 'f':
		hpos += n
		dpos += aim*n

print(hpos*dpos)
