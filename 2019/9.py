import time
from intcode import IntcodeComputer

text = open("9.txt", 'r').read()
# text = open("9test.txt", 'r').read()

def do_part(text, part):
    program = list(map(int, text.split(",")))
    computer = IntcodeComputer(program)
    computer.run(inputs=[part])
    assert len(computer.outputs) == 1
    return computer.outputs[0]

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
