text = open("input13.txt", 'r').read()
# text = open("input13test.txt", 'r').read()

import numpy as np
import re

def parse_machine(machine_text):
    line1, line2, line3 = machine_text.split('\n')
    ax, ay = re.findall(r'\d+', line1)
    bx, by = re.findall(r'\d+', line2)
    prize_xy = re.findall(r'\d+', line3)
    matrix = np.array([[ax, bx], [ay, by]], dtype=int)

    return matrix, np.array(prize_xy, dtype=int)

def solve_machine(machine, const=0):
    eps = 10e-6
    matrix, prize_xy = machine
    prize_xy += const
    a,b = np.linalg.solve(matrix, prize_xy)
    if abs(a-round(a)) > eps or abs(b-round(b)) > eps:
        return 0
    return round(3*a + b)

const = 10000000000000
total1 = 0
total2 = 0
for machine_text in text.split("\n\n"):
    machine = parse_machine(machine_text)
    total1 += solve_machine(machine)
    total2 += solve_machine(machine, const=const)

print(int(total1))
print(int(total2))
# 20669, wrong
# 29505, wrong
# 29512, wrong
# 29517, wrong




# from scipy.optimize import linprog

# def solve_machine(machine):
#     eps = 10e-6
#     matrix, prize_xy = machine

#     # Linear inequality constraints
#     A_ub = None  # No additional inequality constraints
#     b_ub = None  # No additional inequality bounds
    
#     # Objective function coefficients (to minimize 3x1 + x2)
#     c = np.array([3, 1])
    
#     result = linprog(
#         c,              # Objective function coefficients
#         A_ub=A_ub,      # Inequality constraint matrix
#         b_ub=b_ub,      # Inequality constraint vector
#         A_eq=matrix,      # Equality constraint matrix
#         b_eq=prize_xy,      # Equality constraint vector
#         method='highs'  # Most reliable method for equality constraints
#     )
    
#     if type(result.x) == type(None):
#         return 0
#     a,b = result.x
#     if abs(a-round(a)) > eps or abs(b-round(b)) > eps:
#         return 0
#     return int(3*a + b)

