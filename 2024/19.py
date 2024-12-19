text = open("input19.txt", 'r').read()
# text = open("input19test.txt", 'r').read()

from functools import cache

@cache
def can_make(desired, available, cur=""):
    if cur == desired:
        return 1

    total = 0
    for a in available:
        if desired.startswith(cur + a):
            total += can_make(desired, available, cur + a)

    return total

def do_part(part):
    available, desired = text.split("\n\n")
    available = tuple(available.split(", "))
    desired = tuple(desired.split("\n"))
    results = [can_make(d, available) for d in desired]

    if part == 1:
        return sum(1 for x in results if x)

    else:
        return sum(results)


import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
