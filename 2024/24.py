text = open("input24.txt", 'r').read()
# text = open("input24test.txt", 'r').read()

from itertools import combinations

def get_output(gates, values):
    while gates:
        prelen = len(gates)
        newgates = []
        for i1,op,i2,out in gates:
            if i1 in values and i2 in values:
                if out in values: print('error 7834')
                values[out] = operate(values[i1], values[i2], op)
            else:
                newgates.append((i1,op,i2,out))

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

def operate(i1, i2, op):
    if op == "AND": return i1 and i2
    if op == "OR": return i1 or i2
    if op == "XOR": return i1 ^ i2
    print('error 2377')
    return None

def compare(aa, bb):
    return sum(aa[i] == bb[i] for i in range(len(aa)))

def do_part(part):

    values,tmpgates = text.split("\n\n")
    values = dict([(x.split(": ")[0], int(x.split(": ")[1])) for x in values.splitlines()])
    gates = []
    wires = set(values.keys())
    for gate in tmpgates.splitlines():
        i1,op,i2,_,out = gate.split()
        gates.append((i1,op,i2,out))
        wires.add(i1)
        wires.add(i2)
        wires.add(out)

    if part == 1:

        return int(get_output(gates, values), 2)

    else:
        
        output = get_output(gates.copy(), values.copy()).zfill(46)
        expected = get_expected_output(values).zfill(46)
        score = compare(expected, output)

        outputs = [x[3] for x in gates]

        candidates = set()

        for a,b in combinations(outputs, 2):
            xgates = gates.copy()
            for k,xgate in enumerate(xgates):
                if xgate[3] == a:
                    xgates[k] = (xgates[k][0], xgates[k][1], xgates[k][2], b)
                if xgate[3] == b:
                    xgates[k] = (xgates[k][0], xgates[k][1], xgates[k][2], a)

            xoutput = get_output(xgates.copy(), values.copy())

            if xoutput and compare(expected, xoutput.zfill(46)) > score:
                count += 1

        return count


import time
start = time.perf_counter()
print(do_part(1))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
start = time.perf_counter()
print(do_part(2))
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
