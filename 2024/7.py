lines = open("input7.txt", 'r').read().splitlines()
# lines = open("input7test.txt", 'r').read().splitlines()


def combine(s, nn, concat=False):
    if len(nn) == 1:
        if nn[0] == s:
            return True
        return False
    
    if nn[0] > s:
        return False

    x = combine(s, [nn[0]*nn[1]]+nn[2:], concat=concat)
    y = combine(s, [nn[0]+nn[1]]+nn[2:], concat=concat)
    z = False
    if concat:
        z = combine(s, [int(str(nn[0])+str(nn[1]))]+nn[2:], concat=concat)

    return x or y or z


total = 0
total2 = 0
for line in lines:
    test, numbers = line.split(':')
    test = int(test)
    numbers = [int(n) for n in numbers.split()]
    if combine(test, numbers):
        total += test
    if combine(test, numbers, concat=True):
        total2 += test

print(total)
print(total2)
