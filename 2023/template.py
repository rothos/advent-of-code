from math import prod, floor, ceil
from collections import Counter, defaultdict
from itertools import permutations, combinations
import re
from functools import cache

import time
time0 = time.time()

file = "input.txt"
file = "test.txt"

with open(file, 'r') as f:
    content = f.read()
    lines = [list(l) for l in content.split("\n")]


time1 = time.time()
print("%.3fs" % (time1-time0))





time2 = time.time()
print("%.3fs" % (time2-time0))
