file = "input13.txt"
# file = "test13.txt"

def transpose(m):
    a = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return ["".join(p) for p in a]

with open(file, 'r') as f:
    content = f.read()
    blocks = content.split("\n\n")
    blocks = [b.split("\n") for b in blocks]

def checkblock(b):
    for i in range(len(b)-1):
        mirrored = True
        k = 0
        while (i-k)>=0 and (i+1+k)<len(b):
            l1 = b[i-k]
            l2 = b[i+1+k]
            if l1 != l2:
                mirrored = False
                break
            k+=1
        if mirrored == True:
            # for q in range(len(b)):
            #     if i+1==q: print('-'*len(b[0]))
            #     print(str(b[q]))
            # print()
            return i+1

    return False

total = 0
for b in blocks:
    a,c = False, False
    a = checkblock(b)
    if a:
        total += 100*a
    else:
        c = checkblock(transpose(b))
        if c:
            total += c

print(total)
