text = open("input11.txt", 'r').read()
# text = open("input11test.txt", 'r').read()

from functools import cache
import math

@cache
def iterate(n, iters):
    if iters == 0:
        return 1
    if n == 0:
        return iterate(1, iters-1)
    if math.floor(math.log(n, 10)) % 2:
        d = 10 ** ((math.floor(math.log(n, 10)) + 1) / 2)
        return (
                iterate(n // d, iters-1)
              + iterate(n % d, iters-1)
            )
    else:
        return iterate(n*2024, iters-1)

import time
start = time.perf_counter()
nn = list(map(int, text.split()))
print(sum(iterate(n, 25) for n in nn))
print(sum(iterate(n, 75) for n in nn))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
