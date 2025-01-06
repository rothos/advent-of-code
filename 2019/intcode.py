import inspect

INSTRUCTION_LENGTHS = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
    9: 2,
    99: 1,
}

INSTRUCTION_NAMES = {
    1: "ADD",
    2: "MULTIPLY",
    3: "INPUT",
    4: "OUTPUT",
    5: "JUMP-IF-TRUE",
    6: "JUMP-IF-FALSE",
    7: "TEST LESS THAN",
    8: "TEST EQUALS",
    9: "ADJUST RELATIVE BASE",
    99: "HALT",
}

class IntcodeComputer:
    def __init__(self, program=None, **kwargs):
        """
        Exit state settings:
            None: still running
           -1: error
            0: exited with halt code 99
            1: exited due to awaiting input
        """
        self.pos = 0
        self.relative_base = 0
        self.input_index = 0
        self.inputs = []
        self.outputs = []
        self.counter = 0
        self.DEBUG = 0
        self.exit_code = None

        self.set_settings({"program": program, **kwargs})

    def set_settings(self, settings):
        if "inputs" in settings and type(settings["inputs"]) == int:
            settings["inputs"] = [settings["inputs"]]

        for key in settings.keys():
            if type(settings[key]) == list:
                setval = settings[key][:]
            else:
                setval = settings[key]

            if key == "program" and type(setval) == list:
                # Cast list programs to SliceableDicts
                setval = SliceableDict(enumerate(setval))

            if key == "inputs":
                # Only extend the inputs list, don't replace it
                self.inputs.extend(setval)
            else:
                # For all other attrs, set the value
                setattr(self, key, setval)

    def error(self, msg):
        msg = f"ERROR: {msg} in {inspect.currentframe().f_back.f_code.co_name}"
        print(msg)
        return self.exit(-1)

    def write(self, i, val):
        self.program[i] = val

    def read(self, i=None, n=None):
        if i == None:
            i = self.pos
        if n == None:
            return self.program[i]
        else:
            return self.program[i:i+n]

    def get_input(self):
        result = self.inputs[self.input_index]
        self.input_index += 1
        return result

    def output(self, val):
        self.outputs.append(val)

    def exit(self, code, oi=0):
        self.exit_code = code
        return self.outputs[oi:] if code != -1 else None

    def run(self, **kwargs):
        self.set_settings({**kwargs})
        self.exit_code = None
        oi = len(self.outputs)

        if not self.program: self.error("No program provided")
        if self.DEBUG: print(f"Running program (length {len(self.program)})")

        def parse_opcode(num):
            opcode = num % 100
            num //= 100
            num_params = INSTRUCTION_LENGTHS[opcode] - 1
            modes = []
            for k in range(num_params):
                modes.append(num % 10)
                num //= 10
            return opcode, modes

        def interpret_params(last_as_address=False):
            nonlocal params, modes
            ss = []
            for i,p in enumerate(params):
                last = last_as_address and (i == len(params) - 1)
                match modes[i]:
                    case 0:
                        s = self.program[p] if not last else p
                    case 1:
                        assert not last
                        s = p
                    case 2:
                        rel = p + self.relative_base
                        s = self.program[rel] if not last else rel
                ss.append(s)

            return ss

        while True:

            pos = self.pos
            opcode, modes = parse_opcode(self.read())
            instruction = self.read(n=len(modes)+1)
            params = instruction[1:]

            if self.DEBUG: print(f"[{self.counter}] New instruction to {INSTRUCTION_NAMES[opcode]} at pos={self.pos}:")
            if self.DEBUG: print(f"    Instruction: {instruction}")
            if self.DEBUG: print(f"    Parsed opcode as {self.read()} -> opcode={opcode}, modes={modes}")

            increment_pos = True

            match opcode:

                case 1: # ADD [3 params] [@]a + [@]b -> @c
                    a,b,c = interpret_params(True)
                    if self.DEBUG: print(f"    Writing: program[{c}] <- {a} + {b} = {a+b}")
                    self.write(c, a+b)
                
                case 2: # MULTIPLY [3 params] [@]a * [@]b -> @c
                    a,b,c = interpret_params(True)
                    self.write(c, a*b)
                    if self.DEBUG: print(f"    Writing: program[{c}] <- {a} * {b} = {a*b}")
                
                case 3: # INPUT [1 param] input -> @a
                    a, = interpret_params(True)

                    try:
                        self.write(a, self.get_input())
                    except:
                        if self.DEBUG: print("    Exiting: Awaiting input")
                        return self.exit(1, oi)

                    if self.DEBUG: print(f"    New input: program[{a}] <- {self.program[a]}")

                case 4: # OUTPUT [1 param] [@]a -> output
                    a, = interpret_params()
                    self.output(a)
                    if self.DEBUG: print(f"    New output: {a}")

                case 5: # JUMP-IF-TRUE [2 params] if [@]a != 0 jump to [@]b
                    a,b = interpret_params()
                    if a != 0:
                        self.pos = b
                        increment_pos = False
                        if self.DEBUG: print(f"    Jumping: setting pos={b}")
                    else:
                        if self.DEBUG: print(f"    [Do nothing]")

                case 6: # JUMP-IF-FALSE [2 params] if [@]a == 0 jump to [@]b
                    a,b = interpret_params()
                    if a == 0:
                        self.pos = b
                        increment_pos = False
                        if self.DEBUG: print(f"    Jumping: settting pos={b}")
                    else:
                        if self.DEBUG: print(f"    [Do nothing]")

                case 7: # LESS THAN [3 params] if [@]a < [@]b then @c = 1 else @c = 0
                    a,b,c = interpret_params(True)
                    self.program[c] = int(a < b)
                    if self.DEBUG: print(f"    Writing: program[{c}] <- {int(a < b)}")

                case 8: # EQUALS [3 params] if [@]a == [@]b then @c = 1 else @c = 0
                    a,b,c = interpret_params(True)
                    self.program[c] = int(a == b)
                    if self.DEBUG: print(f"    Writing: program[{c}] <- {int(a == b)}")

                case 9: # ADJUST RELATIVE BASE [1 param] relative base += @a
                    a, = interpret_params()
                    if self.DEBUG: print(f"    Updating relative base <- " + \
                        f"{self.relative_base} + {a} = {self.relative_base + a}")
                    self.relative_base += a

                case 99:
                    if self.DEBUG: print(f"Program halted")
                    return self.exit(0, oi)

                case _:
                    self.error(f"Unknown opcode")

            self.counter += 1
            self.pos += increment_pos * INSTRUCTION_LENGTHS[opcode]


class SliceableDict(dict):
    def __getitem__(self, key):
        if isinstance(key, slice):
            # Determine the full range of indices from the slice
            start = key.start if key.start is not None else 0
            stop = key.stop if key.stop is not None else max(self.keys(), default=0) + 1
            step = key.step if key.step is not None else 1
            
            # Generate the range of keys based on the slice
            indices = range(start, stop, step)
            
            # Fetch values, defaulting to 0 if the key is missing
            return [self.get(i, 0) for i in indices]
        
        # For single key access, return 0 if the key doesn't exist
        return self.get(key, 0)
