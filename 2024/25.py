text = open("input25.txt", 'r').read()
# text = open("input25test.txt", 'r').read()

def parse_block(block):
    lines = block.splitlines()
    is_lock = lines[0] == '#####'
    heights = []
    for i in range(5):
        heights.append( sum(line[i] == '#' for line in lines) - 1 )
    return heights, is_lock

def test_lock_and_key(lock, key):
    return all(lock[i]+key[i] <= 5 for i in range(5))

def do_part(part):

    locks = []
    keys = []
    for block in text.split("\n\n"):
        heights, is_lock = parse_block(block)
        if is_lock:
            locks.append(heights)
        else:
            keys.append(heights)

    total = 0
    if part == 1:
        for lock in locks:
            for key in keys:
                if test_lock_and_key(lock, key):
                    total += 1

        return total

    else:
        pass


import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
