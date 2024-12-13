text = open("input13.txt", 'r').read()
# text = open("input13test.txt", 'r').read()

import numpy as np
import re

def parse_machine(machine_text):
    line1, line2, line3 = machine_text.split('\n')
    ax, ay = re.findall(r'\d+', line1)
    bx, by = re.findall(r'\d+', line2)
    prize_xy = re.findall(r'\d+', line3)
    matrix = np.array([[ax, bx], [ay, by]], dtype=float)

    return matrix, np.array(prize_xy, dtype=float)

def solve_machine(machine, const=0):
    matrix, prize_xy = machine
    prize_xy += const
    a,b = np.linalg.solve(matrix, prize_xy)
    a,b = round(a), round(b)
    if not all(matrix @ [a,b] == prize_xy):
        return 0
    return 3*a + b

const = 10_000_000_000_000
total1 = 0
total2 = 0
for machine_text in text.split("\n\n"):
    machine = parse_machine(machine_text)
    total1 += solve_machine(machine)
    total2 += solve_machine(machine, const=const)

print(int(total1))
print(int(total2))
