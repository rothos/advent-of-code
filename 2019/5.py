import time
from intcode import IntcodeComputer

text = open("5.txt", 'r').read(); TEST = False
# text = open("5test.txt", 'r').read(); TEST = True

def do_part(text, part):

    program = list(map(int, text.split(",")))
    computer = IntcodeComputer(program)

    if part == 1:
        
        computer = IntcodeComputer(program)
        state = computer.run(inputs=1)
        return state["outputs"][-1]

    else:

        state = computer.run(inputs=5, GET_USER_INPUT=1 if TEST else 0)
        return state["outputs"][-1]


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
