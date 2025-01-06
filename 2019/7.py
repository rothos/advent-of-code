import time
from intcode import run
import itertools

text = open("7.txt", 'r').read(); TEST = False
# text = open("7test.txt", 'r').read(); TEST = True

def do_part(text, part):

    program = list(map(int, text.split(",")))

    if part == 1:
        
        best = None
        for perm in itertools.permutations(range(5)):
            input_signal = 0
            for k in range(5):
                # First input: Phase signal
                # Second input: Input signal
                program, outputs = run(program, _input=[perm[k], input_signal])
                input_signal = outputs[-1]

            if best == None or input_signal > best:
                best = input_signal

        return best

    else:
        pass


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
