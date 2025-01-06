import time
from intcode import IntcodeComputer
from itertools import permutations

text = open("7.txt", 'r').read()
# text = open("7test.txt", 'r').read()

def do_part(text, part):

    program = list(map(int, text.split(",")))

    if part == 1:

        best = None
        for phase_signal in permutations(range(5)):
            input_signal = 0
            for k in range(5):
                computer = IntcodeComputer(program)
                computer.run(inputs=[phase_signal[k], input_signal])
                assert computer.exit_code == 0
                input_signal = computer.outputs[-1]

            if best == None or input_signal > best:
                best = input_signal

        return best

    else:

        best = None
        best_phase = None
        best_k = None

        for phase_signal in permutations(range(5, 10)):

            amplifiers = [IntcodeComputer(program) for _ in range(5)]
            input_signal = 0
            k = 0

            while True:
                inputs = [input_signal] if k >= 5 else [phase_signal[k%5], input_signal]
                amplifiers[k%5].run(inputs=inputs, name=f"amplifier{k}")
                input_signal = amplifiers[k%5].outputs[-1]

                if all(amplifiers[k].exit_code == 0 for k in range(5)):
                    break

                k += 1

            max_thruster_signal = amplifiers[-1].outputs[-1]
            if best == None or max_thruster_signal > best:
                best = max_thruster_signal
                best_phase = phase_signal
                best_k = k

        return f"{best} (phase = {"".join(str(n) for n in best_phase)}, {(k+1)//5} loops)"


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
