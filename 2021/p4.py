
# part 1

ff = list(open('p4.txt','r').readlines())
ff = [f.strip() for f in ff]

seq = ff[0].split(",")
ff = ff[2:]

def getboards(aa):
    s = '\n'.join(aa)
    boards = s.split('\n\n')
    boards = [b.split('\n') for b in boards]
    boards = [[b[i].split() for i in range(len(b))] for b in boards]
    return boards

boards = getboards(ff)

def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def haswon(markedboard):
    a = [sum(r) for r in markedboard]
    b = [sum(r) for r in transpose(markedboard)]
    if 5 in a or 5 in b:
        return True
    return False

# returns i where seq[i] is the winning number for the given board
def getwindex(board,seq):
    markedboard = [[0,0,0,0,0] for i in range(5)]
    for n_i in range(len(seq)):
        n = seq[n_i]
        for i in range(5):
            for j in range(5):
                if board[i][j] == n:
                    markedboard[i][j] = 1
                    if haswon(markedboard):
                        nsum = sum([(1-markedboard[u][v])*int(board[u][v]) for u in range(5) for v in range(5)])
                        return (n_i,int(seq[n_i]),nsum)

# array of indices of winning number (index of `seq`)
windicies = []

for board in boards:
    windicies += [getwindex(board,seq)]
    if windicies[-1][0] == min([w[0] for w in windicies]):
        print(windicies[-1], windicies[-1][1]*windicies[-1][2])


# part 2

# array of indices of winning number (index of `seq`)
windicies = []

for board in boards:
    windicies += [getwindex(board,seq)]
    if windicies[-1][0] == max([w[0] for w in windicies]):
        print(windicies[-1], windicies[-1][1]*windicies[-1][2])

