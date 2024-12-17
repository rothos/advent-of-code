text = open("input17.txt", 'r').read()
# text = open("input17test.txt", 'r').read()

import re

def parse_input(text):
    abc, p = text.split('\n\n')
    abc = [int(i) for i in re.findall(r'\d+', abc)]
    p = [int(i) for i in p.split()[1].split(",")]
    return abc, p

class Computer():
    def __init__(self, abc, program):
        self.a = abc[0]
        self.b = abc[1]
        self.c = abc[2]
        self.program = program
        self.i = 0

    def __repr__(self):
        return f"a={self.a}, b={self.b}, c={self.c}, i={self.i}"

    def instruct(self, n, lop):
        self.i += 2
        cop = lop
        if lop == 4: cop = self.a
        if lop == 5: cop = self.b
        if lop == 6: cop = self.c
        if lop == 7 and n in [0,2,5,6,7]:
            print(n)
            print('Error #2481')
        
        if n == 0: self.a = self.a // (2**cop)
        if n == 1: self.b = self.b ^ lop
        if n == 2: self.b = cop % 8
        if n == 3 and self.a != 0: self.i = lop
        if n == 4: self.b = self.b ^ self.c
        if n == 5: return cop % 8
        if n == 6: self.b = self.a // (2**cop)
        if n == 7: self.c = self.a // (2**cop)
        return None

    def run(self, a=None):
        if a is not None:
            self.a = a
            self.b = 0
            self.c = 0
            self.i = 0

        returned = None
        outs = []
        while self.i < len(self.program):
            returned = self.instruct(self.program[self.i], self.program[self.i+1])
            if returned != None:
                outs.append(returned)

        return outs

    def get_quine(self, i=None, n=0):
        if i is None:
            i = len(self.program) - 1

        for k in range(8):
            if self.run(a=n*8 + k) == self.program[i:]:
                if i == 0:
                    return n*8 + k
                new = self.get_quine(i=i-1, n=n*8+k)
                if new is not None:
                    return new

        return None

def do_part(part):
    abc, program = parse_input(text)
    com = Computer(abc, program)

    if part == 1:
        outs = com.run()
        return ",".join([str(i) for i in outs])

    else:
        return com.get_quine()

import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
