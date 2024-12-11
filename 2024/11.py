text = open("input11.txt", 'r').read()
# text = open("input11test.txt", 'r').read()

from functools import cache
import math

@cache
def do_iters(n, iters):
    if iters == 0:
        return 1
    if n == 0:
        return do_iters(1, iters-1)
    if math.floor(math.log(n,10)) % 2:
        b = math.floor(math.log(n,10))
        return sum([do_iters(n // 10**(b//2+1), iters-1),
                    do_iters(n % 10**(b//2+1), iters-1)])
    else:
        return do_iters(n*2024, iters-1)

import time
start = time.perf_counter()
nn = list(map(int, text.split()))
print(sum(do_iters(n, 25) for n in nn))
print(sum(do_iters(n, 75) for n in nn))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
