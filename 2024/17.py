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

    def run(self, part):
        returned = None
        outs = []
        while self.i < len(self.program) and (part != 2 or outs == self.program[:len(outs)]):
            returned = self.instruct(self.program[self.i], self.program[self.i+1])
            if returned != None:
                outs.append(returned)
        return outs

def do_part(part):
    # com = Computer([117440,0,0],[0,3,5,4,3,0])
    # out = com.run(2)
    # print(out)
    # exit()

    abc,program = parse_input(text)
    com = Computer(abc, program)

    if part == 1:
        outs = com.run(part)
        return ",".join([str(i) for i in outs])

    else:
        a = 0
        outs = []
        while outs != program:
            com.a = a
            outs = com.run(part)
            # if a % 10000000 == 0:
            #     print(a)
            # if outs:
            #     print(outs)
            #     input("press enter")
            a += 1

        return com.a


import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
