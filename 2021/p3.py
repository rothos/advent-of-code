
# part 1

ff = list(open('p3.txt','r').readlines())
ff = [f.strip() for f in ff]

a = ''
b = ''
for pos in range(len(ff[0])):
    bb = [f[pos] for f in ff]
    com = round(sum([int(b) for b in bb])/float(len(ff)))
    a += str(int(com))

b = "".join(map(lambda x:str(1-int(x)), a))

print(int(a,2)*int(b,2))


# part 2

thisaa = ff.copy()
pos = 0
while len(thisaa) > 1 and pos < len(ff[0]):
    bb = [f[pos] for f in thisaa]
    com = round(sum([int(b) for b in bb])/float(len(thisaa))+.000001)
    thisaa = [f for f in thisaa if f[pos] == str(int(com))]
    pos += 1

a = int(thisaa[0],2)

thisbb = ff.copy()
pos = 0
while len(thisbb) > 1 and pos < len(ff[0]):
    bb = [f[pos] for f in thisbb]
    com = 1-round(sum([int(b) for b in bb])/float(len(thisbb))+.000001)
    thisbb = [f for f in thisbb if f[pos] == str(int(com))]
    pos += 1

b = int(thisbb[0],2)

print(a*b)

