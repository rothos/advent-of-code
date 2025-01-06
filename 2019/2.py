import time
from intcode import IntcodeComputer

text = open("2.txt", 'r').read()
# text = open("2test.txt", 'r').read()

def do_part(text, part):

    program = list(map(int, text.split(",")))
    computer = IntcodeComputer()

    if part == 1:
        program[1] = 12
        program[2] = 2
        state = computer.run(program=program)
        return state["program"][0]

    else:
        target = 19690720
        for noun in range(100):
            for verb in range(100):
                program[1] = noun
                program[2] = verb
                state = computer.run(program=program, pos=0)
                if state["program"][0] == target:
                    return 100*noun + verb


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
