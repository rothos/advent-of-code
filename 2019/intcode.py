import inspect

DEBUG = 0

INSTRUCTION_LENGTHS = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
    99: 1,
}

INSTRUCTION_NAMES = {
    1: "ADD",
    2: "MULTIPLY",
    3: "INPUT",
    4: "OUTPUT",
    5: "JUMP-IF-TRUE",
    6: "JUMP-IF-FALSE",
    7: "LESS THAN",
    8: "EQUALS",
    99: "HALT",
}

def printt(aa):
    for a in aa:
        print(f"  {type(a)}: {a}")

def interpret_params(params, modes, program, as_string=False):
    if type(params) == int:
        params = [params]

    ss = []
    pp = []
    for i,p in enumerate(params):
        if modes[i]:
            ss.append(str(p))
            pp.append(p)
        else:
            ss.append(f"program[{p}]={program[p]}")
            pp.append(program[p])

    if as_string:
        return "[ " + ", ".join(ss) + " ]"
    else:
        return pp

def parse_opcode(num):
    # Mode 0: Parameter mode (params are positions)
    # Mode 1: Immediate mode (params are values)
    s = str(num)
    opcode = int(s[-2:])
    s = s.zfill(1 + INSTRUCTION_LENGTHS[opcode])
    modes = [int(c) for c in s[:-2][::-1]]
    return opcode, modes

def run(_program, _input=None):
    program = _program.copy()
    pos = 0
    outputs = []

    if DEBUG: print(f"Running program (length {len(program)})")
    count = 0

    while True:

        opcode, modes = parse_opcode(program[pos])
        
        num_params = INSTRUCTION_LENGTHS[opcode] - 1
        parameters = program[pos+1:pos+1+num_params]

        if DEBUG: print(f"[{count}] New instruction to {INSTRUCTION_NAMES[opcode]} at pos={pos}:")
        if DEBUG: print(f"    Program: {program[pos:pos+num_params+1]}")
        if DEBUG: print(f"    Parsed opcode as {program[pos]} -> opcode={opcode}, modes={modes}")
        if DEBUG: print(f"    Parameters: {interpret_params(parameters, modes, program, as_string=True)}")

        match opcode:

            case 99:
                if DEBUG: print(f"Program halted")
                return program, outputs
            
            case 1: # ADD [3 params] [@]a + [@]b -> @c
                assert modes[2] == 0
                a,b = interpret_params(program[pos+1:pos+3], modes, program)
                c = program[pos+3]
                if DEBUG: print(f"    Writing: program[{c}] <- {a} + {b} = {a+b}")
                program[c] = a + b
                pos += INSTRUCTION_LENGTHS[opcode]
            
            case 2: # MULTIPLY [3 params] [@]a * [@]b -> @c
                assert modes[2] == 0
                a,b = interpret_params(program[pos+1:pos+3], modes, program)
                c = program[pos+3]
                program[c] = a * b
                if DEBUG: print(f"    Writing: program[{c}] <- {a} * {b} = {a*b}")
                pos += INSTRUCTION_LENGTHS[opcode]
            
            case 3: # INPUT [1 param] input -> @a
                assert modes[0] == 0
                a = program[pos+1]
                if _input == None:
                    print("Input: ", end="")
                program[a] = _input if _input != None else int(input())
                if DEBUG: print(f"    New input: program[{a}] <- {program[a]}")
                pos += INSTRUCTION_LENGTHS[opcode]

            case 4: # OUTPUT [1 param] [@]a -> output
                a, = interpret_params(program[pos+1], modes, program)
                outputs.append(a)
                if DEBUG: print(f"    New output: {a} (program[{a}])")
                # if a != 0 and program[pos+2] != 99:
                #     print(f"ERROR! Diagnostic test failed in " + \
                #         f"{inspect.currentframe().f_code.co_name} (output = {a})")
                pos += INSTRUCTION_LENGTHS[opcode]
            
            case 5: # JUMP-IF-TRUE [2 params] if [@]a != 0 jump to [@]b
                a,b = interpret_params(program[pos+1:pos+3], modes, program)
                if a != 0:
                    pos = b
                    if DEBUG: print(f"    Jumping: setting pos={b}")
                else:
                    pos += INSTRUCTION_LENGTHS[opcode]
                    if DEBUG: print(f"    [Do nothing]")

            case 6: # JUMP-IF-FALSE [2 params] if [@]a == 0 jump to [@]b
                a,b = interpret_params(program[pos+1:pos+3], modes, program)
                if a == 0:
                    pos = b
                    if DEBUG: print(f"    Jumping: settting pos={b}")
                else:
                    pos += INSTRUCTION_LENGTHS[opcode]
                    if DEBUG: print(f"    [Do nothing]")

            case 7: # LESS THAN [3 params] if [@]a < [@]b then @c = 1 else @c = 0
                assert modes[2] == 0
                a,b = interpret_params(program[pos+1:pos+3], modes, program)
                c = program[pos+3]
                program[c] = 1 if a < b else 0
                if DEBUG: print(f"    Writing: program[{c}] <- {1 if a < b else 0}")
                pos += INSTRUCTION_LENGTHS[opcode]

            case 8: # EQUALS [3 params] if [@]a == [@]b then @c = 1 else @c = 0
                assert modes[2] == 0
                a,b = interpret_params(program[pos+1:pos+3], modes, program)
                c = program[pos+3]
                program[c] = 1 if a == b else 0
                if DEBUG: print(f"    Writing: program[{c}] <- {1 if a == b else 0}")
                pos += INSTRUCTION_LENGTHS[opcode]

            case _:
                print(f"ERROR! Unknown opcode in {inspect.currentframe().f_code.co_name}")
                return None

        count += 1
