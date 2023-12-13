file = "input3.txt"
# file = "test3.txt"

import re

### PART 1

with open(file, 'r') as f:
    lines = list(f.readlines())
    lines = [l.strip() for l in lines]

    # Add a border of periods
    lines = ['.'+l+'.' for l in lines]
    dotline = '.'*len(lines[0])
    lines = [dotline] + lines + [dotline]

def find_indices(pattern, s):
    matches = re.finditer(pattern, s)
    indices = [(match.start(), match.end()) for match in matches]
    return indices

# Indices is a tuple of the (start,end) indices of the number
# and lines is a list of three lines of the array (the number
# is in the middle line)
def test_number(indices, lines):
    num = int(lines[1][indices[0]:indices[1]])

    notsymbols = '.0123456789'
    
    # Test all candidates
    j, k = indices[0]-1, indices[1]+1
    if any(c not in notsymbols for c in lines[0][j:k]):
        return num
    if any(c not in notsymbols for c in lines[2][j:k]):
        return num

    if lines[1][j] not in notsymbols or lines[1][k-1] not in notsymbols:
        return num

    return 0

# Search all the lines for numbers near symbols
nums = []
x = re.compile(r"\b\d+\b")
for k,line in enumerate(lines[1:-1]):
    threelines = lines[k:k+3]
    ii = find_indices(x, line)
    for i in ii:
        nums += [test_number(i, threelines)]

print(sum(nums))
# 543867



### PART 2

from math import prod

def get_number_from_index(index, line):
    digits = '0123456789'
    if line[index] not in digits:
        return None

    i,j = index, index+1
    while line[i-1] in digits: i -= 1
    while line[j] in digits: j += 1
    return int(line[i:j])

def find_ratio(index, lines):
    # Find all the numbers this gear is adjacent to
    # and then multiply them.
    # NOTE: This code is buggy ON PURPOSE.
    #       It relies on the fact that no gear has the
    #       SAME NUMBER adjacent to it TWICE.
    nums = set()
    for i in [0,1,2]:
        for j in [index-1,index,index+1]:
            nums.add(get_number_from_index(j, lines[i]))
    nums.remove(None)
    if len(nums) == 2:
        return prod(nums)
    else:
        return 0

# Search all the lines for gears
ratios = []
x = re.compile(r"\*")
for k,line in enumerate(lines[1:-1]):
    threelines = lines[k:k+3]
    ii = find_indices(x, line)
    for i in ii:
        ratios += [find_ratio(i[0], threelines)]

print(sum(ratios))
# 79613331
