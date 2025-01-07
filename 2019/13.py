import time
from intcode import IntcodeComputer

text = open("13.txt", 'r').read()

def chunk_into_triplets(lst):
    return list(zip(*[iter(lst)]*3))

def do_part(text, part):

    program = list(map(int, text.split(",")))
    computer = IntcodeComputer(program)
    outputs = computer.run()
    tiles = {}
    for x,y,z in chunk_into_triplets(outputs):
        tiles[(x,y)] = z

    if part == 1:
        return sum(1 for key in tiles.keys() if tiles[key] == 2)

    else:
        computer = IntcodeComputer(program)
        computer.write(0, 2)
        



def main():
    for part in [1, 2]:
        before = time.perf_counter()
        answer = do_part(text, part)
        after = time.perf_counter()
        elapsed = round((after - before)*1_000_000)
        unit = "µs"
        if elapsed >= 1000:
            elapsed //= 1000
            unit = "ms"
        print(f"Part {part}: {answer} ({elapsed:,} {unit})")

main()
