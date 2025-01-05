import time

text = open("2.txt", 'r').read()
# text = open("2test.txt", 'r').read()


def run(_program):
    program = _program.copy()
    pos = 0
    while True:
        opcode = program[pos]
        match opcode:
            case 99:
                return program
            case 1:
                func = lambda x,y: x + y
            case 2:
                func = lambda x,y: x * y
            case _:
                print("error! unknown opcode")
                return None

        i,j,k = program[pos+1], program[pos+2], program[pos+3]
        program[k] = func(program[i], program[j])
        pos += 4


def do_part(text, part):

    program = list(map(int, text.split(",")))

    if part == 1:
        program[1] = 12
        program[2] = 2
        program = run(program)
        return program[0]

    else:
        target = 19690720
        for noun in range(100):
            for verb in range(100):
                program[1] = noun
                program[2] = verb
                output = run(program)
                if output[0] == target:
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
