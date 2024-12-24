text = open("input24.txt", 'r').read()
# text = open("input24test.txt", 'r').read()

from itertools import combinations

def get_output(gates, values):
    while gates:
        prelen = len(gates)
        newgates = []
        for in1,op,in2,out in gates:
            if in1 in values and in2 in values:
                if out in values: print('error 7834')
                values[out] = operate(values[in1], values[in2], op)
            else:
                newgates.append((in1,op,in2,out))

        gates = newgates.copy()

        if prelen == len(gates) and prelen > 0:
            return None

    zz = sorted([x for x in values.keys() if x[0] == 'z'])[::-1]
    return "".join([str(values[x]) for x in zz])

def get_expected_output(values):
    xx = sorted([x for x in values.keys() if x[0] == 'x'])[::-1]
    yy = sorted([y for y in values.keys() if y[0] == 'y'])[::-1]
    xnum = int("".join([str(values[x]) for x in xx]), 2)
    ynum = int("".join([str(values[y]) for y in yy]), 2)
    return format(xnum + ynum, 'b')

def operate(in1, in2, op):
    if op == "AND": return in1 and in2
    if op == "OR": return in1 or in2
    if op == "XOR": return in1 ^ in2
    print('error 2377')
    return None

def compare(aa, bb):
    return sum(aa[i] != bb[i] for i in range(len(aa)))

def swap_outputs(gates, out1, out2):
    for k,gate in enumerate(gates):
        in1, op, in2, out = gate
        if out == out1:
            gates[k] = (in1, op, in2, out2)
        if out == out2:
            gates[k] = (in1, op, in2, out1)
    return gates

def do_part(part):

    values,tmpgates = text.split("\n\n")
    values = dict([(x.split(": ")[0], int(x.split(": ")[1])) for x in values.splitlines()])
    gates = []
    wires = set(values.keys())
    for gate in tmpgates.splitlines():
        in1,op,in2,_,out = gate.split()
        gates.append((in1,op,in2,out))
        wires.add(in1)
        wires.add(in2)
        wires.add(out)

    if part == 1:

        return int(get_output(gates, values), 2)

    else:

        def get_output_name(input1, input2, operator=None):
            for in1,op,in2,out in gates:
                if sorted([in1, in2]) == sorted([input1, input2]):
                    if not operator or operator == op:
                        return out
            return None

        swaps = [
            ('z14', 'hbk'),
            ('z18', 'kvn'),
            ('z23', 'dbb'),
            ('tfn', 'cvh')
        ]

        names = []
        for a,b in swaps:
            gates = swap_outputs(gates, a, b)
            names.append(a)
            names.append(b)

        #---- Code to verify circuit ----#
        debug = 0
        carry = get_output_name('x00', 'y00', 'AND')
        bitnum = 1

        # Build full adders until something is amiss
        while bitnum < 45:
            in1 = 'x' + str(bitnum).zfill(2)
            in2 = 'y' + str(bitnum).zfill(2)
            expected_zout = 'z' + str(bitnum).zfill(2)
            ins_xor = get_output_name(in1, in2, 'XOR')
            ins_and = get_output_name(in1, in2, 'AND')
            zout = get_output_name(ins_xor, carry, 'XOR')
            tmp = get_output_name(ins_xor, carry, 'AND')

            if debug and zout != expected_zout:
                print("ins_xor:", ins_xor)
                print("ins_and:", ins_and)
                print("zout:", zout)
                print("tmp:", tmp)
            assert zout == expected_zout, f"Error: expected {expected_zout}, got {zout}"

            carry = get_output_name(ins_and, tmp, 'OR')
            if debug:
                print(f"Completed {zout}, carry is {carry}")
            bitnum += 1

        return ",".join(sorted(names))

import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
