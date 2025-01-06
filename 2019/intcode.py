import inspect
from collections import defaultdict

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
        for key in settings.keys():
            if type(settings[key]) == list:
                setval = settings[key][:]
            else:
                setval = settings[key]

            if key == "program" and type(setval) == list:
                # Cast list program to dict
                temp = defaultdict(int)
                temp.update(dict(enumerate(setval)))
                setval = temp

            if key == "inputs":
                # Only extend the inputs list, don't replace it
                self.inputs.extend(setval)
            else:
                # For all other attrs, set the value
                setattr(self, key, setval)

    def write(self, i, val):
        self.program[i] = val

    def read(self, i=None, n=None):
        if i == None:
            i = self.pos
        if n == None:
            return self.program[i]
        else:
            return [self.program[k] for k in range(i,i+n)]

    def input(self):
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

        def get_params(last_as_address=False):
            nonlocal params, modes
            ss = []
            for i,p in enumerate(params):
                last = last_as_address and (i == len(params) - 1)
                match modes[i]:
                    case 0:
                        s = self.read(p) if not last else p
                    case 1:
                        assert not last
                        s = p
                    case 2:
                        addr = p + self.relative_base
                        s = self.read(addr) if not last else addr
                ss.append(s)

            return ss

        def get_params_as_str():
            nonlocal params, modes
            ss = []
            for i,p in enumerate(params):
                match modes[i]:
                    case 0:
                        s = f"program[{p}]={self.read(p)}"
                    case 1:
                        s = str(p)
                    case 2:
                        rel = self.relative_base
                        s = f"program[{p+rel}]={self.read(p+rel)}"
                ss.append(s)

            return ", ".join(ss)

        while True:

            opcode, modes = parse_opcode(self.read())
            instruction = self.read(n=len(modes)+1)
            params = instruction[1:]
            increment_pos = True

            if self.DEBUG: print(f"[{self.counter}] New instruction to {INSTRUCTION_NAMES[opcode]} at pos={self.pos}:")
            if self.DEBUG: print(f"    Instruction: {instruction}")
            if self.DEBUG: print(f"    Parsed {self.read()} as opcode={opcode}, modes={modes}")
            if self.DEBUG: print(f"    Parameters: [ {get_params_as_str()} ]")

            match opcode:

                case 1:
                    # Add
                    a,b,addr = get_params(last_as_address=True)
                    if self.DEBUG: print(f"    Writing: program[{addr}] <- {a} + {b} = {a+b}")
                    self.write(addr, a+b)
                
                case 2:
                    # Multiply
                    a,b,addr = get_params(last_as_address=True)
                    self.write(addr, a*b)
                    if self.DEBUG: print(f"    Writing: program[{addr}] <- {a} * {b} = {a*b}")
                
                case 3:
                    # Input
                    addr, = get_params(last_as_address=True)
                    try:
                        self.write(addr, self.input())
                    except:
                        if self.DEBUG: print("    Exiting: Awaiting input")
                        return self.exit(1, oi)

                    if self.DEBUG: print(f"    New input: program[{addr}] <- {self.read(addr)}")

                case 4:
                    # Output
                    a, = get_params()
                    self.output(a)
                    if self.DEBUG: print(f"    New output: {a}")

                case 5:
                    # Jump-if-true
                    a,b = get_params()
                    if a != 0:
                        self.pos = b
                        increment_pos = False
                        if self.DEBUG: print(f"    Jumping: setting pos={b}")
                    else:
                        if self.DEBUG: print(f"    [Do nothing]")

                case 6:
                    # Jump-if-false
                    a,b = get_params()
                    if a == 0:
                        self.pos = b
                        increment_pos = False
                        if self.DEBUG: print(f"    Jumping: settting pos={b}")
                    else:
                        if self.DEBUG: print(f"    [Do nothing]")

                case 7:
                    # Less than
                    a,b,addr = get_params(last_as_address=True)
                    self.write(addr, int(a < b))
                    if self.DEBUG: print(f"    Writing: program[{addr}] <- {int(a < b)}")

                case 8:
                    # Equals
                    a,b,addr = get_params(last_as_address=True)
                    self.write(addr, int(a == b))
                    if self.DEBUG: print(f"    Writing: program[{addr}] <- {int(a == b)}")

                case 9:
                    # Adjust relative base
                    a, = get_params()
                    if self.DEBUG: print(f"    Updating relative base <- " + \
                        f"{self.relative_base} + {a} = {self.relative_base + a}")
                    self.relative_base += a

                case 99:
                    if self.DEBUG: print(f"Program halted")
                    return self.exit(0, oi)

                case _:
                    raise Exception("Unknown opcode")

            self.counter += 1
            self.pos += increment_pos * INSTRUCTION_LENGTHS[opcode]
