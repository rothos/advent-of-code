from collections import Counter

test = 0

ff = list(open('p6%s.txt' % ('','test')[test], 'r').readlines())[0]
ff = map(int, ff.split(','))
fish = [0]*10

for f in ff:
    fish[f] += 1

def proceed(fish):
    new = fish.pop(0)
    fish.append(0)
    fish[6] += new
    fish[8] += new
    return fish

def sumfish(fish,days):
    fish = [fish[i] for i in range(len(fish))] # copy
    for _ in range(days):
        fish = proceed(fish)
    return sum(fish)

# part 1
print(sumfish(fish,80))

# part 2
print(sumfish(fish,256))
