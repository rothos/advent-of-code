text = open("input21.txt", 'r').read()
text = open("input21test.txt", 'r').read()

import textwrap
from functools import cache

graph = {
    "A^": "<",
    "A<": "v<<",
    "Av": "v<",
    "A>": "v",
    "AA": "",

    "^A": ">",
    "^<": "v<",
    "^v": "v",
    "^>": "v>",
    "^^": "",

    "<^": ">^",
    "<A": ">>^",
    "<v": ">",
    "<>": ">>",
    "<<": "",

    "v^": "^",
    "vA": ">^",
    "v<": "<",
    "v>": ">",
    "vv": "",

    ">^": "<^",
    ">A": "^",
    "><": "<<",
    ">v": "<",
    ">>": "",
}

def process_multiruns(string, curpos, num_runs):
    for _ in range(num_runs):
        string = process(string, curpos=curpos)
        curpos = "A"
    return string

def process_string_as_parts(string):
    outstr = ""
    parts = string.split("A")
    curpos = "A"
    for i,part in enumerate(parts):
        if i != len(parts) - 1:
            part = part + "A"
        outstr += process(part, curpos=curpos)
        curpos = curpos if not len(part) else part[-1]
    return outstr

@cache
def process(string, curpos="A"):
    totals = []
    newstring = ""
    for c in string:
        newstring += graph[curpos + c] + "A"
        curpos = c
    return newstring

def process_part2(string, params):
    num_preruns, num_runs, num_iters = params

    counts = dict()
    for key in graph.keys():
        counts[key] = len(process_multiruns(key[1], key[0], num_runs))

    string = process_multiruns(string, "A", num_preruns+num_runs)
    curpos = "A"

    total = 0
    if num_iters > 1:
        curpos = "A"
        for c in string:
            total += counts[curpos+c]
            curpos = c
    
    return total

def do_part(part):

    strings = [
        (208, "<^AvA^^^Avvv>A"),
        (540, "<^^A<A>vvA>A"),
        (685, "^^A<^AvAvv>A"),
        (879, "<^^^A<A>>AvvvA"),
        (826, "<^^^AvvA^>AvvA")
    ]

    if part == 1:

        totals = []
        for n,string in strings:
            newstring = string
            for k in range(2):
                newstring = process_string_as_parts(newstring)
            totals.append(n * len(newstring))

        return sum(totals)

    else:
        # 1, 12, 12

        for n,string in strings:
            # print(len(process_multiruns(string, "A", 12)))
            # print(process_part2(string, [4, 4, 2]))
            # result = process_part2(string, [0, 6, 2])
            result = process_part2(string, [1, 12, 2])

        return result


        # totals = []
        # for n,string in strings:
        #     newstring = string
        #     for k in range(1):
        #         newstring = process_string_as_parts(newstring)
        #     totals.append(n * len(newstring))
        # return sum(totals)


import time
# start = time.perf_counter()
# print(do_part(1))
# print(f"Execution time: {time.perf_counter() - start:.4f} seconds")

start = time.perf_counter()
print(do_part(2))
# 151659080102 too low
print(f"Execution time: {time.perf_counter() - start:.4f} seconds")
