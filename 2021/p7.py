
test = 0
data = open('p7%s.txt' % ('','test')[test], 'r').readlines()
data = map(int, data[0].split(','))

# Lawrence's one-liner approach:

cost1  = lambda x:  abs(x)
cost2  = lambda x:  abs(x)*(abs(x)+1)/2
getmin = lambda fn: min(sum(fn(pos-d) for d in data) for pos in range(min(data),max(data)))
print(getmin(cost1))
print(getmin(cost2))
