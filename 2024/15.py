# There is a lot of redundant code in here at the moment

text = open("input15.txt", 'r').read()
# text = open("input15test2.txt", 'r').read()
# text = open("input15test.txt", 'r').read()

import numpy as np

def parse_input(t, part):
    m,d = t.split('\n\n')

    if part == 2:
        m = m.replace("#", "##")
        m = m.replace("O", "[]")
        m = m.replace(".", "..")
        m = m.replace("@", "@.")

    m = np.array([list(l) for l in m.split('\n')])
    d = list(d.replace("\n", ""))
    return m,d

def get_direction(instruction):
    if instruction == "v": direction = (1, 0)
    if instruction == "^": direction = (-1, 0)
    if instruction == ">": direction = (0, 1)
    if instruction == "<": direction = (0, -1)
    return direction

def add(a,b):
    return (a[0]+b[0], a[1]+b[1])

def subtract(a,b):
    return (a[0]-b[0], a[1]-b[1])

def print_grid(grid):
    print("\n".join("".join(row) for row in grid))

def do_part(part):
    grid, instructions = parse_input(text, part)
    if part == 1:
        for instruction in instructions:
            direction = get_direction(instruction)
            robot = tuple(np.argwhere(grid == "@")[0])
            loc = robot
            boxes = 0
            while grid[add(loc,direction)] not in ".#":
                loc = add(loc,direction)
                boxes += 1

            if grid[add(loc,direction)] == '.':
                loc = add(loc,direction)
                while boxes > 0:
                    grid[loc] = "O"
                    boxes -= 1
                    loc = subtract(loc, direction)

                grid[loc] = "@"
                grid[robot] = '.'

        print(sum(100*coord[0]+coord[1] for coord in np.argwhere(grid=="O")))
    
    else:
        for instruction in instructions:

            if instruction == "<":
                grid = np.fliplr(grid)

            if instruction in "<>":
                robot = tuple(np.argwhere(grid == "@")[0])
                direction = (0,1)
                loc = robot
                boxes = 0

                while grid[add(loc,direction)] not in ".#":
                    loc = add(loc,direction)
                    if grid[loc] == '[':
                        boxes += 1

                if grid[add(loc,direction)] == '.':
                    loc = add(loc,direction)
                    while boxes > 0:
                        grid[loc] = "[" if instruction == "<" else "]"
                        loc = subtract(loc, direction)
                        grid[loc] = "]" if instruction == "<" else "["
                        boxes -= 1
                        loc = subtract(loc, direction)

                    grid[loc] = "@"
                    grid[robot] = '.'

                if instruction == "<":
                    grid = np.fliplr(grid)

                # continue

            if instruction == "^":
                grid = np.flipud(grid)

            if instruction in "^v":
                robot = tuple(np.argwhere(grid == "@")[0])
                direction = (1,0)
                to_move = [[robot]]
                can_move = True

                while can_move:
                    next_row = []
                    for coord in to_move[-1]:
                        cur = add(coord, direction)
                        if grid[cur] == "#":
                            can_move = False
                            break
                        elif grid[cur] in "[]":
                            next_row.append(cur)
                            if grid[cur] == "[":
                                next_row.append(add(cur, (0,1)))
                            if grid[cur] == "]":
                                next_row.append(add(cur, (0,-1)))

                    if not can_move or not next_row:
                        break

                    to_move.append(next_row)

                if can_move:
                    for coords in to_move[::-1]:
                        coords = set(coords)
                        for coord in coords:
                            grid[add(coord,direction)] = grid[coord]
                            grid[coord] = '.'
                    grid[add(robot,direction)] = '@'
                    grid[robot] = '.'

                if instruction == "^":
                    grid = np.flipud(grid)

        print(sum(100*coord[0]+coord[1] for coord in np.argwhere(grid=="[")))

import time
start = time.perf_counter()
do_part(1)
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
start = time.perf_counter()
do_part(2)
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
