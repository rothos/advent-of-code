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

class IntcodeComputer:
    def __init__(self, settings={}, **kwargs):
        """
        Exit state settings:
            None: still running
           -1: error
            0: exited with halt code 99
            1: exited due to awaiting input
        """
        if type(settings) == list:
            settings = { "program": settings.copy() }

        self.pos = 0
        self.input_counter = 0
        self.inputs = []
        self.outputs = []
        self.instruction_counter = 0
        self.DEBUG = 0
        self.GET_USER_INPUT = 0
        self.set_settings({**(settings or {}), **kwargs})

    def set_settings(self, settings):
        if "inputs" in settings and type(settings["inputs"]) == int:
            settings["inputs"] = [settings["inputs"]]

        for key in settings.keys():
            if type(settings[key]) == list:
                setval = settings[key].copy()
            else:
                setval = settings[key]

            if key == "inputs":
                self.inputs.extend(setval)
            else:
                setattr(self, key, setval)

    def get_return_object(self, exit_code=0, error_msg=""):
        return {
            "program": self.program,
            "inputs": self.inputs,
            "input_counter": self.input_counter,
            "outputs": self.outputs,
            "pos": self.pos,
            "instruction_counter": self.instruction_counter,
            "DEBUG": self.DEBUG,
            "GET_USER_INPUT": self.GET_USER_INPUT,
            "exit_code": exit_code,
            "error_msg": error_msg,
        }

    def interpret_params(self, params, modes, as_string=False):
        if type(params) == int:
            params = [params]

        ss = []
        for i,p in enumerate(params):
            if modes[i]:
                if as_string:
                    ss.append(str(p))
                else:
                    ss.append(p)
            else:
                if as_string:
                    ss.append(f"program[{p}]={self.program[p]}")
                else:
                    ss.append(self.program[p])

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

    @staticmethod
    def get_input(_input, counter):
        if type(_input) == type(lambda x: x):
            return _input(counter)
        else:
            return _input[counter]

    def error(self, msg):
        msg = f"ERROR: {msg} in {inspect.currentframe().f_back.f_code.co_name}"
        print(msg)
        return self.get_return_object(exit_code=-1, error_msg=msg)

    def run(self, settings={}, **kwargs):
        self.set_settings({**(settings or {}), **kwargs})
        self.exit_code = None

        if not self.program: self.error("No program provided")
        if self.DEBUG: print(f"Running program (length {len(self.program)})")
        
        self.instruction_counter = 0

        while True:

            pos = self.pos
            opcode, modes = self.parse_opcode(self.program[pos])
            
            num_params = INSTRUCTION_LENGTHS[opcode] - 1
            parameters = self.program[pos+1:pos+1+num_params]

            if self.DEBUG: print(f"[{self.instruction_counter}] New instruction to {INSTRUCTION_NAMES[opcode]} at pos={self.pos}:")
            if self.DEBUG: print(f"    Program: {self.program[pos:pos+num_params+1]}")
            if self.DEBUG: print(f"    Parsed opcode as {self.program[self.pos]} -> opcode={opcode}, modes={modes}")
            if self.DEBUG: print(f"    Parameters: [ {self.interpret_params(parameters, modes, as_string=True)} ]")

            match opcode:

                case 99:
                    if self.DEBUG: print(f"Program halted")
                    return self.get_return_object(exit_code=0)
                
                case 1: # ADD [3 params] [@]a + [@]b -> @c
                    assert modes[2] == 0
                    a,b = self.interpret_params(self.program[pos+1:pos+3], modes)
                    c = self.program[pos+3]
                    if self.DEBUG: print(f"    Writing: program[{c}] <- {a} + {b} = {a+b}")
                    self.program[c] = a + b
                    self.pos += INSTRUCTION_LENGTHS[opcode]
                
                case 2: # MULTIPLY [3 params] [@]a * [@]b -> @c
                    assert modes[2] == 0
                    a,b = self.interpret_params(self.program[pos+1:pos+3], modes)
                    c = self.program[pos+3]
                    self.program[c] = a * b
                    if self.DEBUG: print(f"    Writing: program[{c}] <- {a} * {b} = {a*b}")
                    self.pos += INSTRUCTION_LENGTHS[opcode]
                
                case 3: # INPUT [1 param] input -> @a
                    assert modes[0] == 0
                    a = self.program[pos+1]

                    if self.GET_USER_INPUT:
                        print("Input: ", end="")
                        _input = int(input())
                    else:
                        try:
                            _input = self.get_input(self.inputs, self.input_counter)
                        except:
                            if self.DEBUG: print("    Exiting: Awaiting input")
                            # Exit with exit_code 1 (awaiting input)
                            return self.get_return_object(exit_code=1)

                    self.program[a] = _input
                    if self.DEBUG: print(f"    New input: program[{a}] <- {self.program[a]}")
                    self.pos += INSTRUCTION_LENGTHS[opcode]
                    self.input_counter += 1

                case 4: # OUTPUT [1 param] [@]a -> output
                    a, = self.interpret_params(self.program[pos+1], modes)
                    self.outputs.append(a)
                    if self.DEBUG: print(
                        f"    New output: {a}{" (" + self.interpret_params(
                                self.program[pos+1], modes, as_string=True
                            ) + ")" if modes[0] == 0 else ""}")
                    # if a != 0 and program[pos+2] != 99:
                    #     print(f"ERROR! Diagnostic test failed in " + \
                    #         f"{inspect.currentframe().f_code.co_name} (output = {a})")
                    self.pos += INSTRUCTION_LENGTHS[opcode]

                case 5: # JUMP-IF-TRUE [2 params] if [@]a != 0 jump to [@]b
                    a,b = self.interpret_params(self.program[pos+1:pos+3], modes)
                    if a != 0:
                        self.pos = b
                        if self.DEBUG: print(f"    Jumping: setting pos={b}")
                    else:
                        self.pos += INSTRUCTION_LENGTHS[opcode]
                        if self.DEBUG: print(f"    [Do nothing]")

                case 6: # JUMP-IF-FALSE [2 params] if [@]a == 0 jump to [@]b
                    a,b = self.interpret_params(self.program[pos+1:pos+3], modes)
                    if a == 0:
                        self.pos = b
                        if self.DEBUG: print(f"    Jumping: settting pos={b}")
                    else:
                        self.pos += INSTRUCTION_LENGTHS[opcode]
                        if self.DEBUG: print(f"    [Do nothing]")

                case 7: # LESS THAN [3 params] if [@]a < [@]b then @c = 1 else @c = 0
                    assert modes[2] == 0
                    a,b = self.interpret_params(self.program[pos+1:pos+3], modes)
                    c = self.program[pos+3]
                    self.program[c] = 1 if a < b else 0
                    if self.DEBUG: print(f"    Writing: program[{c}] <- {1 if a < b else 0}")
                    self.pos += INSTRUCTION_LENGTHS[opcode]

                case 8: # EQUALS [3 params] if [@]a == [@]b then @c = 1 else @c = 0
                    assert modes[2] == 0
                    a,b = self.interpret_params(self.program[pos+1:pos+3], modes)
                    c = self.program[pos+3]
                    self.program[c] = 1 if a == b else 0
                    if self.DEBUG: print(f"    Writing: program[{c}] <- {1 if a == b else 0}")
                    self.pos += INSTRUCTION_LENGTHS[opcode]

                case _:
                    self.error(f"Unknown opcode")

            self.instruction_counter += 1
