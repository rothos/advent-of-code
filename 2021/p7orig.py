
test = 0
data = open('p7%s.txt' % ('','test')[test], 'r').readlines()
data = map(int, data[0].split(','))

# Part 1

winner_k    = 0
winner_cost = 10**9
for k in range(max(data)):
    cost = sum([abs(d-k) for d in data])
    if cost < winner_cost:
        winner_cost = cost
        winner_k = k

print(winner_k, winner_cost)

# Part 2

winner_k    = 0
winner_cost = 10**9
T = lambda n: n*(n+1)/2
for k in range(max(data)):
    cost = sum([T(abs(d-k)) for d in data])
    if cost < winner_cost:
        winner_cost = cost
        winner_k = k

print(winner_k, winner_cost)
