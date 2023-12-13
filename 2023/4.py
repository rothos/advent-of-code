file = "input4.txt"
# file = "test4.txt"

### PART 1

with open(file, 'r') as f:
    lines = list(f.readlines())
    lines = [l.strip() for l in lines]

points = []
matches = []
for line in lines:
    data = line.split(':')[1].strip()
    winners, numbers = data.split("|")
    winners = list(map(int, filter(lambda x: x, winners.strip().split(" "))))
    numbers = list(map(int, filter(lambda x: x, numbers.strip().split(" "))))
    wins = list(filter(lambda a: a in winners, numbers))
    if wins:
        points += [2**(len(wins)-1)]
        matches += [len(wins)]
    else:
        matches += [0]

print(sum(points))

### PART 2

copies = {}
for n in range(len(matches)):
    copies[n] = 1

for n in range(len(matches)):
    c = copies[n]
    m = matches[n]
    for j in range(m):
        copies[n+j+1] += c

print(sum(copies.values()))
