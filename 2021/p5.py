
# parts 1 and 2

ff = list(open('p5.txt','r').readlines())
ff = [f.strip() for f in ff]

for i in range(len(ff)):
    ff[i] = ff[i].split(' -> ')
    ff[i] = [[int(t) for t in g.split(',')] for g in ff[i]]

vecs = ff
land1 = [[0 for i in range(1001)] for x in range(1001)]
land2 = [[0 for i in range(1001)] for x in range(1001)]

def isVertHorz(vec):
    if vec[0][0] == vec[1][0] or vec[0][1] == vec[1][1]:
        return True
    return False

def isVert(vec):
    if vec[0][0] == vec[1][0]:
        return True
    return False

for vec in vecs:
    if not isVertHorz(vec):
        xi = vec[0][0]
        yi = vec[0][1]
        while xi != vec[1][0]:
            while yi != vec[1][1]:
                land2[yi][xi] += 1
                xi += 1 if vec[0][0] < vec[1][0] else -1
                yi += 1 if vec[0][1] < vec[1][1] else -1
        land2[yi][xi] += 1
    else:
        if isVert(vec):
            xx = [vec[0][1],vec[1][1]]
            y = vec[0][0]
            for xi in range(min(xx),max(xx)+1):
                land1[xi][y] += 1
                land2[xi][y] += 1
        else:
            yy = [vec[0][0],vec[1][0]]
            x = vec[0][1]
            for yi in range(min(yy),max(yy)+1):
                land1[x][yi] += 1
                land2[x][yi] += 1

# for x in land:print("".join([str(i) if i>0 else "." for i in x]))

print(sum([sum([p >= 2 for p in la]) for la in land1]))
print(sum([sum([p >= 2 for p in la]) for la in land2]))
