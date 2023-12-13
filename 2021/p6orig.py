from collections import Counter

test = 0

ff = list(open('p6%s.txt' % ('','test')[test], 'r').readlines())[0]
ff = map(int, ff.split(','))
fish = dict(Counter(ff))

def proceed(fish):
    new = dict((n,0) for n in range(9))
    for k in fish.keys():
        if k == 0:
            new[8] += fish[k]
            new[6] += fish[k]
        else:
            new[k-1] += fish[k]
    return new

def sumfish(fish,days):
    for day in range(days):
        fish = proceed(fish)
    return sum([fish[k] for k in fish.keys()])

# part 1
print(sumfish(fish,80))

# part 2
print(sumfish(fish,256))

