from functools import cache

file = "input12.txt"
# file = "test12.txt"

with open(file, "r") as f:
    lines = list([l.strip() for l in f.readlines()])
    lines = [l.split(" ") for l in lines]
    tt = [l[0] for l in lines]
    ll = [tuple(map(int,l[1].split(','))) for l in lines]

@cache
def recurse(line, ll, expect=None):
    # print(line,ll,expect)

    if not line:
        if not ll or (len(ll)==0 and ll[0]==0):
            return 1
        return 0

    if not ll:
        if '#' in line:
            return 0
        return 1

    if ll[0] < 0:
        return 0

    newll = tuple([ll[0]-1]+list(ll[1:]))

    if not expect:
        if line[0] == ".":
            return recurse(line[1:],ll[:])
        if line[0] == "#":
            
            if newll[0] == 0:
                return recurse(line[1:],newll[1:],".")
            else:
                return recurse(line[1:],newll,"#")
        if line[0] == "?":
            total = 0
            total += recurse(line[1:],ll[:])

            if newll[0] == 0:
                total +=  recurse(line[1:],newll[1:],".")
            else:
                total +=  recurse(line[1:],newll,"#")
            
            return total

    elif expect == ".":
        if line[0] == "#":
            return 0
        return recurse(line[1:],ll[:])

    elif expect == "#":
        if line[0] == ".":
            return 0
        if newll[0] == 0:
            return recurse(line[1:],newll[1:],".")
        else:
            return recurse(line[1:],newll,"#")

    print("ERROR:",line,ll,expect)

total = []
for i in range(len(tt)):
    total += [recurse(tt[i]+"?"+tt[i]+"?"+tt[i]+"?"+tt[i]+"?"+tt[i], ll[i]*5)]

# print(total)
print(sum(total))
