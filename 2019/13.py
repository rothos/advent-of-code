import time
from intcode import IntcodeComputer

text = open("13.txt", 'r').read()
USER_INPUT = 0
DEBUG = 0

def print_screen(tiles):
    print(f"Score: {tiles[(-1,0)]}")
    tmap = {
        0: " ",
        1: "▒",
        2: "X", #█
        3: "▔",
        4: "●"
    }
    maxx = max(xy[0] for xy in tiles.keys())
    maxy = max(xy[1] for xy in tiles.keys())
    for y in range(0, maxy + 1):
        s = ""
        for x in range(0, maxx + 1):
            s += tmap[tiles[(x,y)]]
        print(s)

def print_and_wait(tiles):
    if USER_INPUT or DEBUG:
        print_screen(tiles)
        if not USER_INPUT: input()

def chunk_into_triplets(lst):
    return list(zip(*[iter(lst)]*3))

def add(x, y):
    return [x[0]+y[0], x[1]+y[1]]

def subtract(x, y):
    return [x[0]-y[0], x[1]-y[1]]

def do_part(text, part):

    tiles = {}
    lastball = None

    def update_tiles(outputs):
        nonlocal tiles
        for x,y,z in chunk_into_triplets(outputs):
            tiles[(x,y)] = z

    def get_input():
        if USER_INPUT:
            # User play
            key = input() or "d"
            if key[0] in "sj": return -1
            if key[0] in "fl": return 1
            return 0

        else:
            # Bot play
            nonlocal tiles, lastball

            def get_paddle(): return [key for key in tiles.keys() if tiles[key] == 3][0]
            def get_ball():   return [key for key in tiles.keys() if tiles[key] == 4][0]
            def is_empty(xy): return tiles[xy] == 0
            def is_wall(xy):  return tiles[xy] == 1
            def is_block(xy): return tiles[xy] == 2

            ball = get_ball()
            paddle = get_paddle()

            # On the first frame, do nothing
            if not lastball:
                lastball = ball
                return 0

            # If ball is directly above paddle, do nothing
            if ball[0] == paddle[0] and (ball[1] + 1) == paddle[1]:
                lastball = ball
                return 0

            # Else, follow the ball
            balldir = subtract(ball, lastball)
            nextball = add(ball, balldir)
            lastball = ball
            if paddle[0] < nextball[0]: return 1
            if paddle[0] > nextball[0]: return -1
            return 0

    program = list(map(int, text.split(",")))

    if part == 1:
        computer = IntcodeComputer(program)
        update_tiles(computer.run())
        return sum(1 for key in tiles.keys() if tiles[key] == 2)

    else:
        computer = IntcodeComputer(program)
        computer.write(0, 2)
        update_tiles(computer.run())
        print_and_wait(tiles)
        while computer.exit_code != 0:
            update_tiles(computer.run(inputs=[get_input()]))
            print_and_wait(tiles)

        return tiles[(-1,0)]

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
