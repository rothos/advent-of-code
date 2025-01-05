import time
from intcode import run

text = open("5.txt", 'r').read(); TEST = False
# text = open("5test.txt", 'r').read(); TEST = True

def do_part(text, part):

    program = list(map(int, text.split(",")))

    if part == 1:
        
        program, outputs = run(program, _input=1)
        return outputs[-1]

    else:

        _input = None if TEST else 5
        program, outputs = run(program, _input=_input)
        return outputs[-1]


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
