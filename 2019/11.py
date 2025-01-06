import time
from intcode import IntcodeComputer
from collections import defaultdict

text = open("11.txt", 'r').read()

def rotate(vec, reverse=0):
    x, y = vec
    return (y, -x) if reverse else (-y, x)

def add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def print_panels(panels):
    minx = min(xy[0] for xy in panels.keys()) - 1
    maxx = max(xy[0] for xy in panels.keys()) + 1
    miny = min(xy[1] for xy in panels.keys()) - 2
    maxy = max(xy[1] for xy in panels.keys()) + 1

    for y in range(maxy, miny, -1):
        s = ""
        for x in range(minx, maxx):
            s += "#" if panels[(x,y)] else "."
        print(s)


def do_part(text, part):

    program = list(map(int, text.split(",")))

    computer = IntcodeComputer(program)
    panels = defaultdict(int)
    location = (0, 0)
    direction = (0, 1)

    if part == 2:
        panels[location] = 1

    while computer.exit_code != 0:
        color, reverse = computer.run(inputs=panels[location])
        panels[location] = color
        direction = rotate(direction, reverse=reverse)
        location = add(location, direction)

    if part == 1:
        return len(panels)

    else:
        print_panels(panels)
        return "See image ^"


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
