from math import prod, floor, ceil
from collections import Counter, defaultdict
from itertools import permutations, combinations
import re

file = "input14.txt"
# file = "test14.txt"

### PART 1

with open(file, 'r') as f:
    content = f.read()
    lines = content.split("\n")
