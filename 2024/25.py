text = open("input25.txt", 'r').read()
# text = open("input25test.txt", 'r').read()

def parse_block(block):
    lines = block.splitlines()
    is_lock = lines[0] == '#####'
    heights = []
    for i in range(5):
        heights.append( sum(line[i] == '#' for line in lines) - 1 )
    return heights, is_lock

def go():
    locks = []
    keys = []
    for block in text.split("\n\n"):
        heights, is_lock = parse_block(block)
        if is_lock:
            locks.append(heights)
        else:
            keys.append(heights)

    total = 0
    for lock in locks:
        for key in keys:
            total += all(lock[i]+key[i] <= 5 for i in range(5))

    return total


import time
start = time.perf_counter()
print(go())
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
