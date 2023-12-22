from math import prod, floor, ceil
from collections import Counter, defaultdict
from itertools import permutations, combinations
import re
from functools import cache

import time
time0 = time.time()

file = "input19.txt"
# file = "test19.txt"

with open(file, 'r') as f:
    content = f.read()
    tmprules, parts = content.split("\n\n")
    
    tmprules = tmprules.split("\n")
    rules = dict()
    for rule in tmprules:
        name, rest = rule.split("{")
        rest = rest[:-1].split(",")
        pairs = []
        for r in rest:
            if ":" in r:
                a,b = r.split(":")
                end = b
                if b=="R": end = False
                if b=="A": end = True
                pairs.append((a,end))
            else:
                end = r
                if r=="R": end = False
                if r=="A": end = True
                pairs.append(("True", end))
        rules[name] = pairs

    parts = parts.split("\n")
    parts = [p[1:-1].replace(",",";") for p in parts]


ans = 0

for part in parts:
    result = "in"
    exec(part)
    while result not in [True, False]:
        
        condlist = rules[result]
        for cond,res in condlist:
            if eval(cond):
                result = res
                break
        else:
            print("ERROR: loop didn't break ::", part, condlist)


    if result:
        ans += x+m+a+s

print(ans)

time1 = time.time()
print("-- %.3fs --" % (time1-time0))
