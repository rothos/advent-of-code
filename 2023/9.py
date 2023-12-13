with open("input9.txt", "r") as f:
# with open("test9.txt", "r") as f:
    lines = list(f.readlines())
    ss1 = [[int(k) for k in l.split()] for l in lines]
    ss2 = [s[::-1] for s in ss1]

def nextnum(s):
    ss = [s]
    while not all(n==0 for n in ss[-1]):
        s = ss[-1] + [0]
        ww = []
        for i in range(1,len(s)):
            ww += [s[i] - s[i-1]]
        del ww[-1]
        ss += [ww]

    ss[-1].append(0)
    ss = list(reversed(ss))
    for i in range(1,len(ss)):
        ss[i].append(ss[i][-1]+ss[i-1][-1])

    return ss[-1][-1]

print(sum(nextnum(s) for s in ss1))

print(sum(nextnum(s) for s in ss2))
