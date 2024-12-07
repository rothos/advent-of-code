lines = open("input7.txt", 'r').read().splitlines()
# lines = open("input7test.txt", 'r').read().splitlines()

import re

def combine(s, nn, concat=False):
    if len(nn) == 1:
        return nn[0] == s
    
    if nn[0] > s:
        return False

    return (
        combine(s, [nn[0]*nn[1]]+nn[2:], concat=concat)
        or combine(s, [nn[0]+nn[1]]+nn[2:], concat=concat)
        or (concat and combine(s, [int(str(nn[0])+str(nn[1]))]+nn[2:], concat=concat))
    )


total = total2 = 0
for line in lines:
    desired, *values = map(int, re.split(':? ', line))
    if combine(desired, values):
        total += desired
    if combine(desired, values, concat=True):
        total2 += desired

print(total)
print(total2)
