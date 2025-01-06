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
                input_signal = computer.outputs[-1]

            if best == None or input_signal > best:
                best = input_signal

        return best

    else:

        best = None
        for phase_signal in permutations(range(5, 10)):
            amplifiers = [IntcodeComputer(program, inputs=[phase_signal[i]]) for i in range(5)]
            input_signal = 0
            k = -1
            while 1+(k := k + 1) and not all(amplifiers[i].exit_code == 0 for i in range(5)):
                amplifiers[k%5].run(inputs=[input_signal])
                input_signal = amplifiers[k%5].outputs[-1]

            max_thruster_signal = amplifiers[-1].outputs[-1]
            if best == None or max_thruster_signal > best:
                best = max_thruster_signal

        return best

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
