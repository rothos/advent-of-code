text = open("input22.txt", 'r').read()
# text = open("input22test.txt", 'r').read()

from collections import defaultdict
from functools import cache
import numpy as np

@cache
def get_secrets(n, iters=2000):
    array = [n]
    for _ in range(iters):
        n = (n ^ (n*64)) % 16777216
        n = (n ^ (n//32)) % 16777216
        n = (n ^ (n*2048)) % 16777216
        array.append(n)
    return array

def make_map(n):
    secrets = get_secrets(n, 2000)
    prices = [s%10 for s in secrets]
    diffs = [int(i) for i in np.diff(prices)]
    pmap = defaultdict(int)
    for k in range(len(diffs)-3):
        subseq = tuple(diffs[k:k+4])
        if subseq not in pmap.keys():
            pmap[subseq] = prices[k+4]
    return pmap

def do_part(part):
    nn = [int(n) for n in text.splitlines()]

    if part == 1:
        return sum(get_secrets(n, 2000)[-1] for n in nn)

    else:
        pmaps = [make_map(n) for n in nn]

        subseqs = set()
        for pmap in pmaps:
            subseqs |= set(pmap.keys())

        best = -99999
        for subseq in subseqs:
            score = sum(pmap[subseq] for pmap in pmaps)
            if score > best:
                best = score

        return best

import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
