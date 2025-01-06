import time
from intcode import IntcodeComputer

text = open("5.txt", 'r').read(); TEST = 0
# text = open("5test.txt", 'r').read(); TEST = 1

def do_part(text, part):

    program = list(map(int, text.split(",")))
    computer = IntcodeComputer(program)

    if part == 1:
        
        computer = IntcodeComputer(program)
        computer.run(inputs=1)
        return computer.outputs[-1]

    else:

        computer.run(inputs=5, GET_USER_INPUT=TEST)
        return computer.outputs[-1]


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
