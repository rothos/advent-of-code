from math import prod, floor, ceil
from collections import Counter, defaultdict
from itertools import permutations, combinations
import re

file = "input15.txt"
# file = "test15.txt"

### PART 1

with open(file, 'r') as f:
    content = f.read().replace("\n","").split(",")

def hash1(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val = val % 256
    return val

vals = []
for part in content:
    vals += [hash1(part)]

print(sum(vals))




boxes = [[] for i in range(256)]

for part in content:

    if "-" in part:
        parts = part.split("-")
        label = parts[0]
        boxnum = hash1(label)

        lenses = boxes[boxnum]
        for i,l in enumerate(lenses):
            if label == l.split(" ")[0]:
                del boxes[boxnum][i]
                break

    elif "=" in part:
        parts = part.split("=")
        label = parts[0]
        boxnum = hash1(label)
        power = int(parts[1])

        lenses = boxes[boxnum]
        for i,l in enumerate(lenses):
            if label == l.split(" ")[0]:
                boxes[boxnum][i] = label + " " + str(power)
                break
        else:
            boxes[boxnum] += [label + " " + str(power)]

ans = 0
for i,box in enumerate(boxes):
    for j,lens in enumerate(box):
        power = int(lens.split()[1])
        ans += (i+1) * (j+1) * int(power)

print(ans)
