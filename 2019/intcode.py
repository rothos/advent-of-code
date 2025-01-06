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
            2: exited because reached MAX_ITERS
        """
        self.pos = 0
        self.relative_base = 0
        self.input_index = 0
        self.inputs = []
        self.outputs = []
        self.outputs_from_this_run = []
        self.instruction_counter = 0
        self.DEBUG = 0
        self.GET_USER_INPUT = 0
        self.MAX_ITERS = 0
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

    def interpret_params(self, params, modes, last_as_address=False, as_string=False):
        # Note: The program will break if BOTH last_as_address & as_string are set to True.
        if type(params) == int:
            params = [params]

        ss = []
        for i,p in enumerate(params):
            match modes[i]:
                case 0:
                    if last_as_address and i == len(params) - 1:
                        s = p
                    else:
                        s = self.program[p] if not as_string else f"program[{p}]={self.program[p]}"
                case 1:
                    s = p if not as_string else str(p)
                case 2:
                    if last_as_address and i == len(params) - 1:
                        s = p + self.relative_base
                    else:
                        s = self.program[p + self.relative_base] if not as_string \
                            else f"program[{p}+{self.relative_base}]={self.program[p + self.relative_base]}"
            ss.append(s)

        if as_string:
            return ", ".join(ss)
        else:
            return ss

    @staticmethod
    def parse_opcode(num):
        # Accepts: integer
        # Returns: opcode, list of parameter modes
        #
        # Mode 0: Parameter mode (params are positions)
        # Mode 1: Immediate mode (params are values)
        s = str(num)
        opcode = int(s[-2:])
        s = s.zfill(1 + INSTRUCTION_LENGTHS[opcode])
        modes = [int(c) for c in s[:-2][::-1]]
        return opcode, modes

    def error(self, msg):
        msg = f"ERROR: {msg} in {inspect.currentframe().f_back.f_code.co_name}"
        print(msg)
        self.exit_code = -1
        return self.outputs_from_this_run

    def run(self, **kwargs):
        self.set_settings({**kwargs})
        self.exit_code = None
        self.outputs_from_this_run = []

        if not self.program: self.error("No program provided")
        if self.DEBUG: print(f"Running program (length {len(self.program)})")

        while True:

            if self.MAX_ITERS and self.instruction_counter > self.MAX_ITERS:
                self.exit_code = 2
                return self.outputs_from_this_run

            pos = self.pos
            opcode, modes = self.parse_opcode(self.program[pos])

            num_params = INSTRUCTION_LENGTHS[opcode] - 1
            program_slice = self.program[pos:pos+num_params+1]
            params = program_slice[1:]

            if self.DEBUG: print(f"[{self.instruction_counter}] New instruction to {INSTRUCTION_NAMES[opcode]} at pos={self.pos}:")
            if self.DEBUG: print(f"    Program: {program_slice}")
            if self.DEBUG: print(f"    Parsed opcode as {self.program[pos]} -> opcode={opcode}, modes={modes}")
            if self.DEBUG: print(f"    Parameters: [ {self.interpret_params(params, modes, as_string=True)} ]")

            increment_pos = True

            match opcode:

                case 1: # ADD [3 params] [@]a + [@]b -> @c
                    assert modes[2] != 1
                    a,b,c = self.interpret_params(program_slice[1:], modes, last_as_address=True)
                    if self.DEBUG: print(f"    Writing: program[{c}] <- {a} + {b} = {a+b}")
                    self.program[c] = a + b
                
                case 2: # MULTIPLY [3 params] [@]a * [@]b -> @c
                    assert modes[2] != 1
                    a,b,c = self.interpret_params(program_slice[1:], modes, last_as_address=True)
                    self.program[c] = a * b
                    if self.DEBUG: print(f"    Writing: program[{c}] <- {a} * {b} = {a*b}")
                
                case 3: # INPUT [1 param] input -> @a
                    assert modes[0] != 1
                    a, = self.interpret_params(program_slice[1], modes, last_as_address=True)

                    if self.GET_USER_INPUT:
                        print("Input: ", end="")
                        _input = int(input())
                    else:
                        try:
                            _input = self.inputs[self.input_index]
                        except:
                            if self.DEBUG: print("    Exiting: Awaiting input")
                            # Exit with exit_code 1 (awaiting input)
                            self.exit_code = 1
                            return self.outputs_from_this_run

                    self.program[a] = _input
                    if self.DEBUG: print(f"    New input: program[{a}] <- {self.program[a]}")
                    self.input_index += 1

                case 4: # OUTPUT [1 param] [@]a -> output
                    a, = self.interpret_params(program_slice[1], modes)
                    self.outputs.append(a)
                    self.outputs_from_this_run.append(a)
                    if self.DEBUG:
                        print(f"    New output: {a}{" (" + self.interpret_params(
                                program_slice[1], modes, as_string=True
                            ) + ")" if modes[0] == 0 else ""}")

                case 5: # JUMP-IF-TRUE [2 params] if [@]a != 0 jump to [@]b
                    a,b = self.interpret_params(program_slice[1:], modes)
                    if a != 0:
                        self.pos = b
                        increment_pos = False
                        if self.DEBUG: print(f"    Jumping: setting pos={b}")
                    else:
                        if self.DEBUG: print(f"    [Do nothing]")

                case 6: # JUMP-IF-FALSE [2 params] if [@]a == 0 jump to [@]b
                    a,b = self.interpret_params(program_slice[1:], modes)
                    if a == 0:
                        self.pos = b
                        increment_pos = False
                        if self.DEBUG: print(f"    Jumping: settting pos={b}")
                    else:
                        if self.DEBUG: print(f"    [Do nothing]")

                case 7: # LESS THAN [3 params] if [@]a < [@]b then @c = 1 else @c = 0
                    assert modes[2] != 1
                    a,b,c = self.interpret_params(program_slice[1:], modes, last_as_address=True)
                    self.program[c] = int(a < b)
                    if self.DEBUG: print(f"    Writing: program[{c}] <- {int(a < b)}")

                case 8: # EQUALS [3 params] if [@]a == [@]b then @c = 1 else @c = 0
                    assert modes[2] != 1
                    a,b,c = self.interpret_params(program_slice[1:], modes, last_as_address=True)
                    self.program[c] = int(a == b)
                    if self.DEBUG: print(f"    Writing: program[{c}] <- {int(a == b)}")

                case 9: # ADJUST RELATIVE BASE [1 param] relative base += [@]a
                    # TODO: for opcode 209, shouldn't last_as_address=True?
                    #       i'd have to update something. it errors out right now for that.
                    a, = self.interpret_params(program_slice[1], modes)
                    if self.DEBUG: print(f"    Updating relative base <- " + \
                        f"{self.relative_base} + {a} = {self.relative_base + a}")
                    self.relative_base += a

                case 99:
                    if self.DEBUG: print(f"Program halted")
                    self.exit_code = 0
                    return self.outputs_from_this_run

                case _:
                    self.error(f"Unknown opcode")

            self.instruction_counter += 1
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
